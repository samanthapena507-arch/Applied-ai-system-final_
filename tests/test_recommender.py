import pytest

from src.recommender import (
    Song,
    UserProfile,
    Recommender,
    score_song,
    recommend_songs,
)

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def make_song_dicts():
    return [
        {
            "id": 1,
            "title": "Exact-ish Match",
            "artist": "Test Artist",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        {
            "id": 2,
            "title": "Different Song",
            "artist": "Test Artist",
            "genre": "rock",
            "mood": "sad",
            "energy": 0.2,
            "tempo_bpm": 70,
            "valence": 0.1,
            "danceability": 0.2,
            "acousticness": 0.9,
        },
    ]


def test_recommend_songs_with_missing_targets_relies_on_order_when_scores_tie():
    songs = make_song_dicts()
    user_prefs = {"genre": "metal"}

    ranked = recommend_songs(user_prefs, songs, k=2)

    assert ranked[0][1] == 0.0
    assert ranked[1][1] == 0.0
    assert ranked[0][0]["id"] == 1
    assert ranked[1][0]["id"] == 2


def test_score_song_out_of_range_targets_clamp_to_zero_similarity():
    song = make_song_dicts()[0]
    user_prefs = {
        "energy": 5,
        "tempo_bpm": -200,
        "valence": 2,
        "danceability": -3,
        "acousticness": 4,
    }

    score, reasons = score_song(user_prefs, song)

    assert score == 0.0
    assert len(reasons) == 5
    assert all("similarity 0.00" in reason for reason in reasons)


def test_score_song_normalizes_case_and_whitespace_for_categorical_match():
    song = make_song_dicts()[0]
    user_prefs = {"genre": "  POP ", "mood": " HaPpY "}

    score, reasons = score_song(user_prefs, song)

    assert score == 3.0
    assert "genre match (+1.00)" in reasons
    assert "mood match (+2.00)" in reasons


def test_score_song_raises_for_non_numeric_values():
    song = make_song_dicts()[0]
    user_prefs = {"energy": "high"}

    with pytest.raises(ValueError):
        score_song(user_prefs, song)


def test_empty_categorical_strings_skip_bonuses_and_keep_numeric_scoring():
    song = make_song_dicts()[0]
    user_prefs = {"genre": "", "mood": "   ", "energy": 0.8}

    score, reasons = score_song(user_prefs, song)

    assert score == pytest.approx(0.30)
    assert all("match" not in reason for reason in reasons)
    assert reasons == ["energy similarity 1.00 (+0.30)"]
