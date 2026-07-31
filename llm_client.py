"""Thin wrapper around the Gemini API for generating recommendation explanations."""
import json
import os
import re

from google import genai


class GeminiClient:
    """Calls Gemini to generate a natural-language recommendation explanation."""

    def __init__(self, model_name: str = "gemini-flash-lite-latest", temperature: float = 0.2):
        api_key = os.getenv("GEMINI_API_KEY", "").strip()
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set")
        self._client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.temperature = temperature

    def generate_explanation(self, prompt: str) -> str:
        response = self._client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={"temperature": self.temperature},
        )
        return (response.text or "").strip()

    def parse_preferences(self, text: str) -> dict:
        """Aggregate a listener's free-text description into a structured
        preference profile: keywords/genres, per-feature weights, and a
        single best-representing genre. Raises if Gemini doesn't return
        parseable JSON, so callers should have a fallback in place.
        """
        prompt = (
            "You are the preference-parsing step of a music recommender. "
            "A listener described what they want to hear in free text below. "
            "Identify the keywords/genres they mentioned, weigh each numeric "
            "feature by how much emphasis the listener gave it, and pick the "
            "single genre that best represents their overall request.\n\n"
            f'Listener text: "{text}"\n\n'
            "Respond with ONLY valid JSON (no markdown fences, no commentary) "
            "matching exactly this shape:\n"
            "{\n"
            '  "keywords": ["...", "..."],\n'
            '  "genre": "...",\n'
            '  "mood": "...",\n'
            '  "energy": 0.0,\n'
            '  "tempo_bpm": 120.0,\n'
            '  "valence": 0.0,\n'
            '  "danceability": 0.0,\n'
            '  "acousticness": 0.0,\n'
            '  "weights": {"energy": 0.0, "tempo_bpm": 0.0, "valence": 0.0, "danceability": 0.0, "acousticness": 0.0},\n'
            '  "best_genre": "...",\n'
            '  "keyword_reference": "One sentence naming the specific keywords that led to best_genre."\n'
            "}\n"
            "All fields except tempo_bpm must be between 0 and 1. Weights should sum to roughly 1.0."
        )
        raw = self.generate_explanation(prompt)
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        json_text = match.group(0) if match else raw
        return json.loads(json_text)
