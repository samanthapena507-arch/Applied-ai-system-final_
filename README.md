# 🎵 Music Recommender Simulation 2.0

## Original Recommender Simulation Summary
The original Music recommender model SongSavenger 1.0 was a recommender that would load the songs in the songs.csv file and based on hardcoded user prefrences and ranks them. The model was able to deal with dierect mood and genre matches as well as case sensitivity

## Title and Summary

**Music Recommender Simulation** 
The new recommender uses a gemini pass key to add in a fine tune and specialized element to the recommender. The new version takes in a comma seperated list of keywords for what the kind of song the user wants to get recommendations for. The system then uses the song data in songs.csv to come up with the top five songs closest to what the user wants similar to the original model. 

This new change matters as it can now be more flexible with the users input and adds a UI element to make the recommender cleaner. This new recommender helps with the direct mood and genre match limitations of the original model as well. 

---

## Architecture Overview

The system has two implementations of the same idea, both diagrammed of which are in the mermaid.mmd file in the diagrams folder

1. **Functional scoring path** (`load_songs` → `recommend_songs` → `score_song`) — loads the songs from the soongs.csv file  into dictionaries, then for each song computes a score made of:
   - Categorical bonuses: +1.00 for a genre match, +2.00 for a mood match.
   - Weighted numerical similarity: for energy, tempo, valence, danceability, and acousticness, similarity is `1 - |song_value - target_value| / scale`, weighted by `energy(0.30)`, `tempo(0.25)`, `valence(0.20)`, `danceability(0.15)`, `acousticness(0.10)`.
   
   Songs are then sorted by total score and the top `k` number of songs are returned along with a list of reasons.

2. **OOP path** (`Recommender` / `Song` / `UserProfile`) — wraps songs and a user profile as dataclasses and exposes `recommend()` and `explain_recommendation()`. Explanations come from a heuristic (comparing genre/mood/energy) by default, or from the Gemini API when one is configured, with the heuristic as a fallback if the Gemini API call fails or returns nothing.
`main.py` puts these two implementations together as the CLI entry point and the `gui.py` provides a Tkinter desktop UI over the same recommender logic. Both are then launched automatically at the end of `main()`.

Design notes and the reasoning behind the scoring recipe (including known biases toward mood over genre and higher weighted features) are in the model_card.md file.

---

## Setup Instructions

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Enable LLM-generated explanations by creating a `.env` file with:

   ```
   GEMINI_API_KEY=your-key-here
   ```

   Without a key, the recommender falls back to heuristic explanations automatically.

4. Run the CLI (this also launches the Tkinter GUI window at the end):

   ```bash
   python main.py
   ```

---

## Sample Recommendation Output

```
OG design
=================================================================
Top recommendations:

#1 Sunrise City
Final Score: 3.29
Reasons:
  - genre match (+1.00)
  - mood match (+2.00)
  - energy similarity 0.98 (+0.29)
--------------------------------------------------
#2 Rooftop Lights
Final Score: 2.29
Reasons:
  - mood match (+2.00)
  - energy similarity 0.96 (+0.29)
--------------------------------------------------
#3 Golden Hour Drift
Final Score: 2.27
Reasons:
  - mood match (+2.00)
  - energy similarity 0.91 (+0.27)
--------------------------------------------------
#4 Gym Hero
Final Score: 1.26
Reasons:
  - genre match (+1.00)
  - energy similarity 0.87 (+0.26)
--------------------------------------------------
#5 Afterglow Avenue
Final Score: 0.30
Reasons:
  - energy similarity 0.99 (+0.30)
--------------------------------------------------
=================================================================

New design with Gemini

Example 1:
=================================================================
Keywords detected: upbeat, happy, pop, dance energy
Best representing genre: pop
The keywords 'upbeat', 'happy', and 'pop' directly led to the selection of pop as the best genre.

======================================================================

#1 Sunrise City
Final Score: 3.95
Reasons:
  - genre match (+1.00)
  - mood match (+2.00)
  - energy similarity 0.97 (+0.29)
  - tempo_bpm similarity 0.95 (+0.10)
  - valence similarity 0.94 (+0.28)
  - danceability similarity 0.94 (+0.28)
  - acousticness similarity 0.92 (+0.00)
AI Explanation: You'll love "Sunrise City" by Neon Echo because its joyful pop sound and high-energy vibe (0.82) are practically made to match your upbeat taste!
--------------------------------------------------
#2 Rooftop Lights
Final Score: 2.94
Reasons:
  - mood match (+2.00)
  - energy similarity 0.91 (+0.27)
  - tempo_bpm similarity 1.00 (+0.10)
  - valence similarity 0.91 (+0.27)
  - danceability similarity 0.97 (+0.29)
  - acousticness similarity 0.75 (+0.00)
AI Explanation: You're going to love "Rooftop Lights" by Indigo Parade because its joyful indie pop vibe and high-energy beat (0.76) hit that happy, upbeat sweet spot you're looking for!
--------------------------------------------------
#3 Golden Hour Drift
Final Score: 2.92
Reasons:
  - mood match (+2.00)
  - energy similarity 0.86 (+0.26)
  - tempo_bpm similarity 0.98 (+0.10)
  - valence similarity 0.93 (+0.28)
  - danceability similarity 0.95 (+0.29)
  - acousticness similarity 0.86 (+0.00)
AI Explanation: You'll love "Golden Hour Drift" by Marble Sky because its bright indie pop sound delivers plenty of happy, sun-soaked vibes! While its energy is a tiny bit below your usual target, it still brings a wonderfully uplifting and vibrant beat that will keep you smiling.
--------------------------------------------------
#4 Gym Hero
Final Score: 1.92
Reasons:
  - genre match (+1.00)
  - energy similarity 0.92 (+0.28)
  - tempo_bpm similarity 0.93 (+0.09)
  - valence similarity 0.87 (+0.26)
  - danceability similarity 0.97 (+0.29)
  - acousticness similarity 0.95 (+0.00)
AI Explanation: You're going to love "Gym Hero" by Max Pulse because its super high energy (0.93) hits right near your 0.85 target! Plus, its intense pop vibes will totally give you that fun, upbeat mood you're looking for.
--------------------------------------------------
#5 Neon Alley
Final Score: 0.89
Reasons:
  - energy similarity 0.99 (+0.30)
  - tempo_bpm similarity 0.77 (+0.08)
  - valence similarity 0.72 (+0.22)
  - danceability similarity 0.99 (+0.30)
  - acousticness similarity 0.98 (+0.00)
AI Explanation: If you love upbeat pop, you'll adore "Neon Alley" by Chrome River because its high energy level of 0.84 matches your vibe, while its confident hip-hop rhythm brings a fun, feel-good bounce to your day!
--------------------------------------------------
=================================================================

Example 2:
=================================================================
Keywords detected: emo, sad, high energy, danceable
Best representing genre: Dance-Punk
The combination of high energy and danceability paired with emo and sad led to the selection of Dance-Punk.

======================================================================

#1 Afterglow Avenue
Final Score: 0.91
Reasons:
  - energy similarity 0.94 (+0.33)
  - tempo_bpm similarity 0.82 (+0.12)
  - valence similarity 0.79 (+0.08)
  - danceability similarity 0.96 (+0.29)
  - acousticness similarity 0.91 (+0.09)
AI Explanation: You’re going to love "Afterglow Avenue" by Static Bloom because its high-energy synthwave sound hits that exact 0.79 sweet spot you're looking for. It delivers that driving, dance-ready tempo you want, paired with a moody, melancholic vibe that feels just like a late-night dance-punk anthem!
--------------------------------------------------
#2 Sunrise City
Final Score: 0.90
Reasons:
  - energy similarity 0.97 (+0.34)
  - tempo_bpm similarity 0.86 (+0.13)
  - valence similarity 0.46 (+0.05)
  - danceability similarity 0.99 (+0.30)
  - acousticness similarity 0.92 (+0.09)
AI Explanation: Even though "Sunrise City" leans a bit happier than your usual melancholy tastes, its high-energy vibe (0.82) is a great match for the driving pulse you love in Dance-Punk! Plus, its vibrant pop sound is sure to give you that upbeat, late-night rush you're looking for.
--------------------------------------------------
#3 Late Night Signals
Final Score: 0.90
Reasons:
  - energy similarity 0.89 (+0.31)
  - tempo_bpm similarity 0.94 (+0.14)
  - valence similarity 0.86 (+0.09)
  - danceability similarity 0.89 (+0.27)
  - acousticness similarity 0.97 (+0.10)
AI Explanation: You'll love "Late Night Signals" by Pulse Theory because its intense, high-energy EDM sound hits that exact 0.96 pulse you're looking for, delivering the perfect driving beat for your dance-punk cravings!
--------------------------------------------------
#4 Storm Runner
Final Score: 0.90
Reasons:
  - energy similarity 0.94 (+0.33)
  - tempo_bpm similarity 0.86 (+0.13)
  - valence similarity 0.82 (+0.08)
  - danceability similarity 0.86 (+0.26)
  - acousticness similarity 1.00 (+0.10)
AI Explanation: You're going to love "Storm Runner" by Voltline because its intense, high-energy rock vibe (sitting right at that 0.91 mark!) hits that exact sweet spot of being both melancholic and fiercely energetic. It's the ultimate adrenaline rush for any dance-punk fan looking to move fast while still soaking in those moody undertones!
--------------------------------------------------
#5 Neon Alley
Final Score: 0.90
Reasons:
  - energy similarity 0.99 (+0.35)
  - tempo_bpm similarity 0.68 (+0.10)
  - valence similarity 0.68 (+0.07)
  - danceability similarity 0.94 (+0.28)
  - acousticness similarity 0.98 (+0.10)
AI Explanation: "Neon Alley" was recommended because its high energy (0.84) hits that exact 0.85 target you're looking for, while bringing a confident, genre-bending vibe that pairs surprisingly well with melancholic dance-punk.
--------------------------------------------------
=================================================================

Eaxmple 3:
=================================================================
Keywords detected: sad, low energy, danceable, pop, acoustic
Best representing genre: pop
The explicit mention of 'pop' combined with 'acoustic' and 'danceable' directly points to acoustic-driven sad pop music.

======================================================================

#1 Sunrise City
Final Score: 1.55
Reasons:
  - genre match (+1.00)
  - energy similarity 0.38 (+0.10)
  - tempo_bpm similarity 0.81 (+0.08)
  - valence similarity 0.36 (+0.07)
  - danceability similarity 0.91 (+0.23)
  - acousticness similarity 0.38 (+0.08)
AI Explanation: Oops, it looks like our playlist generator had a bit of a mix-up and suggested the upbeat, happy tracks when you were actually in the mood for some chill, melancholy pop! We'll make sure to dial down the energy next time so you get those cozy, sad-pop vibes you're looking for.
--------------------------------------------------
#2 Gym Hero
Final Score: 1.48
Reasons:
  - genre match (+1.00)
  - energy similarity 0.27 (+0.07)
  - tempo_bpm similarity 0.69 (+0.07)
  - valence similarity 0.43 (+0.09)
  - danceability similarity 0.82 (+0.20)
  - acousticness similarity 0.25 (+0.05)
AI Explanation: Even though you usually prefer a lower-energy, mellow vibe, "Gym Hero" is a fun pop curveball that brings an intense and powerful punch to your playlist!
--------------------------------------------------
#3 Focus Flow
Final Score: 0.83
Reasons:
  - energy similarity 0.80 (+0.20)
  - tempo_bpm similarity 0.88 (+0.09)
  - valence similarity 0.61 (+0.12)
  - danceability similarity 0.90 (+0.23)
  - acousticness similarity 0.98 (+0.20)
AI Explanation: If you're in the mood for some reflective pop, you'll love how "Focus Flow" by LoRoom blends gentle lofi beats with a dedicated, focused vibe. Even though its energy is slightly higher at 0.4, its mellow atmosphere hits that sweet spot for a calm, introspective listening session!
--------------------------------------------------
#4 Library Rain
Final Score: 0.82
Reasons:
  - energy similarity 0.85 (+0.21)
  - tempo_bpm similarity 0.81 (+0.08)
  - valence similarity 0.60 (+0.12)
  - danceability similarity 0.88 (+0.22)
  - acousticness similarity 0.94 (+0.19)
AI Explanation: If you're in the mood for some down-tempo pop, you'll love "Library Rain" by Paper Lanterns! Its gentle, chill lofi vibes and soothingly low energy hit that sweet spot for a cozy, melancholic rainy day.
--------------------------------------------------
#5 Midnight Coding
Final Score: 0.82
Reasons:
  - energy similarity 0.78 (+0.20)
  - tempo_bpm similarity 0.86 (+0.09)
  - valence similarity 0.64 (+0.13)
  - danceability similarity 0.92 (+0.23)
  - acousticness similarity 0.91 (+0.18)
AI Explanation: If you love sad pop, you'll probably enjoy the mellow, late-night vibes of "Midnight Coding" by LoRoom. Even though its energy is a tiny bit higher than your usual target, its chill lofi sound makes it the perfect comforting background track for a quiet, melancholic evening.
--------------------------------------------------
=================================================================
---
```
## Design Decisions

When it came to the design of the projects improvements I wanted to find a way to make the recommender more useable and flexible. The area I wanted to target was where the previous model failed in genre and mood. Though still limited to whats in the songs.csv file I wanted the system to be able to identify a sort of hierarchy when it came to genre and mood. This later eveolved into the use of simple key words entered into the gemini helper that was intergated into the program. Through these key words and the new system logic the system no longer has to rely on hard coded values for a users prefrences. 
The tradeoffs I made were the catalogue limitations and easier real time testing as I could no longer enter the data of a song in directly for the users tastes to see if the system would recognize it like I did in the original. 

## Testing summary

Most of the testing I did was runtime testing to see how the system would react to different inputs from the user. 
One of the tests I did was similar to the one I did in the original program where I input keywords to try and get a specific genre from the recommender which ended in the system giving me the results I was going for. I also did a test where no keywords or a single letter was entered to see what they system would do. For this test they system was able to handle this gracefully and even gave a default list of default songs were displayed with an explanation of why the deafault was presented. This made me realize just how well the AI assisted program was able to handle unfit data as well as how it can be intuitive. It was able to easily recognize the genre I was going for without having to input the genre as a keyword. This also showed me just how much the us of AI in projects can improve the flexiblity of a program making it ore user friendly. 

|Input |Evaluation |Result |
|------|-----------|-------|
|h |Gave default results |Pass|
|sad, low energy, danceable, pop, acoustic |Defaulted to mostly lofi not pop |Partial pass|
| happy, traditional, family, danceable, acoustic |Gave intended genre of Folk |Pass|

---

## Limitations and Risks

- Only works on a tiny catalog so far but accuracy would likely improve with more songs. However, more songs would cost the programm at runtime.
- Doesn't understand lyrics, language, or content — a song can match numerically while still being inappropriate for the listener which is why the songs cataloge is limited to the ones in songs.csv so far.
- Tends to favor happy/pop leaning profiles over metal leaning ones, and favors mood matches over genre matches due to the weighting scheme that I put into the logic layer.

---

## Reflection

This project taught me a bit about time management like some of my others but also about the complexities of working with AI and implementing AI faetures into one of the programs that I create. I'd say the hardest part was getting started as it felt like a big step, but once the ideas and plans become clearer with thought, the rest of the project started to flow.
Read the full reflection and design rationale in [model_card.md](model_card.md).
