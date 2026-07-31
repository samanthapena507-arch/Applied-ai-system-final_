"""Tkinter GUI for the Music Recommender Simulation.

The listener types a free-text description of what they want to hear.
That text is sent to Gemini, which aggregates it into keywords/genres
(weighted by emphasis) and a single best-representing genre. The result
drives the existing scoring pipeline in recommender.py.
"""
import tkinter as tk
from tkinter import messagebox, scrolledtext

if __package__:
    from .recommender import Recommender, Song, UserProfile, recommend_songs
else:
    from recommender import Recommender, Song, UserProfile, recommend_songs

KNOWN_GENRES = {"pop", "indie pop", "lofi", "metal", "rock", "chill"}


def _fallback_parse(text: str) -> dict:
    """Naive local aggregation used when Gemini is unavailable or errors out."""
    keywords = [word.strip().lower() for word in text.replace(",", " ").split() if word.strip()]
    best_genre = next((word for word in keywords if word in KNOWN_GENRES), keywords[0] if keywords else "pop")
    return {
        "keywords": keywords,
        "genre": best_genre,
        "mood": "neutral",
        "energy": 0.5,
        "tempo_bpm": 120.0,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.5,
        "weights": {"energy": 0.3, "tempo_bpm": 0.25, "valence": 0.2, "danceability": 0.15, "acousticness": 0.1},
        "best_genre": best_genre,
        "keyword_reference": f"Gemini unavailable; used keywords {keywords} directly as a rough match.",
    }


class RecommenderGUI:
    def __init__(self, root: tk.Tk, songs: list, client=None):
        self.songs = songs
        self.client = client
        self.recommender = Recommender([Song(**song) for song in songs], client=client)

        root.title("Music Recommender")
        root.geometry("760x620")

        tk.Label(root, text="Describe what you want to hear:").pack(anchor="w", padx=10, pady=(10, 0))

        entry_frame = tk.Frame(root)
        entry_frame.pack(fill="x", padx=10, pady=5)

        self.input_entry = tk.Entry(entry_frame)
        self.input_entry.insert(0, "upbeat happy pop with a bit of dance energy")
        self.input_entry.pack(side="left", fill="x", expand=True)
        self.input_entry.bind("<Return>", lambda _event: self.on_submit())

        tk.Button(entry_frame, text="Get Recommendations", command=self.on_submit).pack(side="left", padx=(8, 0))

        status = "Gemini connected" if client is not None else "Gemini not configured (using local fallback)"
        tk.Label(root, text=status, fg="gray").pack(anchor="w", padx=10)

        self.output = scrolledtext.ScrolledText(root, wrap="word", state="disabled")
        self.output.pack(padx=10, pady=10, fill="both", expand=True)

    def on_submit(self) -> None:
        text = self.input_entry.get().strip()
        if not text:
            messagebox.showwarning("Input needed", "Describe what you want to hear first.")
            return

        if self.client is not None:
            try:
                parsed = self.client.parse_preferences(text)
            except Exception as exc:
                parsed = _fallback_parse(text)
                parsed["keyword_reference"] += f" (Gemini call failed: {exc})"
        else:
            parsed = _fallback_parse(text)

        user_prefs = {
            "genre": parsed.get("genre") or parsed.get("best_genre", ""),
            "mood": parsed.get("mood", ""),
            "energy": parsed.get("energy"),
            "tempo_bpm": parsed.get("tempo_bpm"),
            "valence": parsed.get("valence"),
            "danceability": parsed.get("danceability"),
            "acousticness": parsed.get("acousticness"),
            "weights": parsed.get("weights", {}),
        }
        user_prefs = {key: value for key, value in user_prefs.items() if value is not None}

        recommendations = recommend_songs(user_prefs, self.songs, k=5)

        user_profile = UserProfile(
            favorite_genre=user_prefs.get("genre", ""),
            favorite_mood=user_prefs.get("mood", ""),
            target_energy=user_prefs.get("energy", 0.5),
            likes_acoustic=user_prefs.get("acousticness", 0) >= 0.5,
        )

        self._render(parsed, recommendations, user_profile)

    def _render(self, parsed: dict, recommendations: list, user_profile: UserProfile) -> None:
        self.output.configure(state="normal")
        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, f"Keywords detected: {', '.join(parsed.get('keywords', []))}\n")
        self.output.insert(tk.END, f"Best representing genre: {parsed.get('best_genre', 'unknown')}\n")
        self.output.insert(tk.END, f"{parsed.get('keyword_reference', '')}\n")
        self.output.insert(tk.END, "\n" + "=" * 70 + "\n\n")

        for index, (song, score, explanation) in enumerate(recommendations, start=1):
            self.output.insert(tk.END, f"#{index} {song['title']}\n")
            self.output.insert(tk.END, f"Final Score: {score:.2f}\n")
            self.output.insert(tk.END, "Reasons:\n")
            for line in explanation.splitlines():
                self.output.insert(tk.END, f"  {line}\n")

            ai_explanation = self.recommender.explain_recommendation(user_profile, Song(**song))
            self.output.insert(tk.END, f"AI Explanation: {ai_explanation}\n")
            self.output.insert(tk.END, "-" * 50 + "\n")

        self.output.configure(state="disabled")


def launch_gui(songs: list, client=None) -> None:
    root = tk.Tk()
    RecommenderGUI(root, songs, client)
    root.mainloop()
