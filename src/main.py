"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # test made to match perfectly to the song Rooftop Lights in songs.csv
    user_prefs2 = {"genre": "indie pop", "mood": "happy", "energy": 0.76, "tempo_bpm": 124, "valence": 0.81, "danceability": 0.82, "acousticness": 0.35}

    recommendations = recommend_songs(user_prefs2, songs, k=5)

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
        print("-" * 50)
    
    print("Loaded songs:", len(songs))

if __name__ == "__main__":
    main()
