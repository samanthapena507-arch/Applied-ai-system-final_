import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song], client=None):
        """Initialize the recommender with the available songs.

        `client` is an optional object exposing generate_explanation(prompt: str) -> str
        (e.g. llm_client.GeminiClient). When omitted, explanations fall back to a
        heuristic built from the user/song attributes.
        """
        self.songs = songs
        self.client = client

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return up to k recommended songs for the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a given song was recommended for the user."""
        heuristic = self._heuristic_explanation(user, song)
        if self.client is None:
            return heuristic

        try:
            explanation = self.client.generate_explanation(self._build_prompt(user, song))
            return explanation if explanation.strip() else heuristic
        except Exception:
            return heuristic

    def _build_prompt(self, user: UserProfile, song: Song) -> str:
        return (
            f'Explain in 1-2 friendly sentences why the song "{song.title}" by {song.artist} '
            f"was recommended to a listener who likes {user.favorite_genre} music with a "
            f"{user.favorite_mood} mood and a target energy of {user.target_energy}. "
            f"The song's genre is {song.genre}, its mood is {song.mood}, and its energy is {song.energy}."
        )

    def _heuristic_explanation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append(f"matches your favorite genre ({song.genre})")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append(f"matches your favorite mood ({song.mood})")
        if abs(song.energy - user.target_energy) < 0.15:
            reasons.append("has a similar energy level to what you like")

        if not reasons:
            return f'"{song.title}" was included based on overall similarity to your taste profile.'
        return f'"{song.title}" was recommended because it ' + " and ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into typed dictionaries."""
    songs: List[Dict] = []
    numeric_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key == "id":
                    song[key] = int(value)
                elif key in numeric_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a preference score and explanation reasons for one song."""
    score = 0.0
    reasons: List[str] = []

    def _norm_text(value: Optional[str]) -> str:
        """Normalize text values for case-insensitive preference matching."""
        if value is None:
            return ""
        return str(value).strip().lower()

    # Categorical bonuses
    user_genre = _norm_text(user_prefs.get("genre"))
    song_genre = _norm_text(song.get("genre"))
    if user_genre and song_genre and user_genre == song_genre:
        score += 1.0
        reasons.append("genre match (+1.00)")

    user_mood = _norm_text(user_prefs.get("mood"))
    song_mood = _norm_text(song.get("mood"))
    if user_mood and song_mood and user_mood == song_mood:
        score += 2.0
        reasons.append("mood match (+2.00)")

    # Numerical preference weights (defaults from README algorithm recipe).
    default_weights: Dict[str, float] = {
        "energy": 0.30,
        "tempo_bpm": 0.25,
        "valence": 0.20,
        "danceability": 0.15,
        "acousticness": 0.10,
    }

    user_weight_overrides = user_prefs.get("weights", {})
    weights = dict(default_weights)
    if isinstance(user_weight_overrides, dict):
        for key, value in user_weight_overrides.items():
            normalized_key = "valence" if key == "valance" else key
            if normalized_key in weights:
                weights[normalized_key] = float(value)

    # Scale used to normalize distance into a [0, 1] similarity.
    # Most features are in [0, 1]. Tempo uses BPM, so we normalize over 120 BPM.
    field_specs = (
        ("energy", ("energy",), 1.0),
        ("tempo_bpm", ("tempo_bpm", "tempo"), 120.0),
        ("valence", ("valence", "valance"), 1.0),
        ("danceability", ("danceability",), 1.0),
        ("acousticness", ("acousticness", "acoustic"), 1.0),
    )

    for song_field, pref_aliases, scale in field_specs:
        target_value = None
        for pref_key in pref_aliases:
            if pref_key in user_prefs:
                target_value = user_prefs[pref_key]
                break

        if target_value is None or song_field not in song:
            continue

        target = float(target_value)
        song_value = float(song[song_field])
        distance = abs(song_value - target)
        similarity = max(0.0, 1.0 - (distance / scale))
        weighted_points = similarity * weights[song_field]
        score += weighted_points
        reasons.append(f"{song_field} similarity {similarity:.2f} (+{weighted_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k with explanations."""
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "\n".join(f"- {reason}" for reason in reasons)
        if not explanation:
            explanation = "- No specific preference matches found."
        scored.append((song, score, explanation))

    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]
