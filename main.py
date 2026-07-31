"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
import os

from dotenv import load_dotenv

if __package__:
    from .recommender import load_songs, recommend_songs, Recommender, Song, UserProfile
    from .gui import launch_gui
else:
    from recommender import load_songs, recommend_songs, Recommender, Song, UserProfile
    from gui import launch_gui

load_dotenv()


def build_gemini_client():
    """Return a GeminiClient if GEMINI_API_KEY is set, otherwise None."""
    if not os.getenv("GEMINI_API_KEY", "").strip():
        return None
    try:
        if __package__:
            from .llm_client import GeminiClient
        else:
            from llm_client import GeminiClient
        return GeminiClient()
    except Exception:
        return None


def main() -> None:
    songs = load_songs("data/songs.csv")
    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # test made to match perfectly to the song Rooftop Lights in songs.csv
    user_prefs2 = {"genre": "indie pop", "mood": "happy", "energy": 0.76, "tempo_bpm": 124, "valence": 0.81, "danceability": 0.82, "acousticness": 0.35}
    # alternative tests
    user_prefs3 = {"genre": "lofi", "mood": "focused", "energy": 0.5, "tempo": 80, "valence": 0.65}
    user_prefs4 = {"genre": "metal", "mood": "chill", "energy": 0.65, "tempo_bpm": 125, "valance": 0.8, "danceability": 0.7, "acoustic": 0.4}
    # my profile
    my_prefs = {"genre": "indie pop", "mood": "happy", "energy": 0.75, "tempo": 130, "valence": 0.8, "danceability": 0.93, "acousticness": 0.6}

    recommendations = recommend_songs(user_prefs3, songs, k=5)

    client = build_gemini_client()
    recommender = Recommender([Song(**song) for song in songs], client=client)
    user_profile = UserProfile(
        favorite_genre=user_prefs3["genre"],
        favorite_mood=user_prefs3["mood"],
        target_energy=user_prefs3["energy"],
        likes_acoustic=user_prefs3.get("acousticness", 0) >= 0.5,
    )

    print("\nTop recommendations:\n")
    for index, rec in enumerate(recommendations, start=1):
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"#{index} {song['title']}")
        print(f"Final Score: {score:.2f}")
        print("Reasons:")
        for line in explanation.splitlines():
            print(f"  {line}")
        ai_explanation = recommender.explain_recommendation(user_profile, Song(**song))
        print(f"AI Explanation: {ai_explanation}")
        print("-" * 50)

    print("Loaded songs:", len(songs))

    launch_gui(songs, client)

if __name__ == "__main__":
    main()
