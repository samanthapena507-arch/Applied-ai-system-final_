# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

- three things that are used when picking songs: likes, dislikes, and subscriptions/artist follows. Also a mix of content based filtering and collaborative 

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real world recommenders:
From my understanding of platforms like Spotifiy and YouTube they use a combination of content-based filtering, collaborative filtering, and other behavioral signals. These signals include things such as likes, dislikes, and subscriptions/artist follows. These signals are presented during further use of the platform. These kinds of systems are powered by machine learning and are adaptable to the users changing tastes.

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
Each song in the system will have numeric attributes for the energy, tempo, dancability, acousticness, and valance. Then string attributes for the genre and mood. It will also have a final score that will be used to determine its rank later
- What information does your `UserProfile` store
The user will mirror what the song has in a sense as it will have a prefered energy, tempo, danceability, acousticness, and valance score from 1-10 and then a prefered range of genres and moods.
- How does your `Recommender` compute a score for each song
The recommender computes a score for each song based on the songs distance from the users prefrences for each of the songs attributes. It will also create a list of the songs in order from most similar to least similar to the users prefrences.
- How do you choose which songs to recommend
after calculating the songs score from the numeric values it will then get a bonus if it is a genre and or mood match. the songs with the highest scores will then be first in the ranking.

You can include a simple diagram or bullet list if helpful.

- Algorithm Recipe:
Points for songs are rewarded for their similarity to the users prefrences. For prefrences like genre and mood points are given as bonous points where a matching mood gets 2 points and a matching genre gets 1. For the number based prefrences points are rewarded based on distance from the target number (e.g. the user prefrence). The weights for the numerical prefrences will be as follows: energy(0.3), tempo(0.25), valance(0.20), danceability(0.15), acoustic(0.1). 
- potential biases:
The probable biases that will come up in the system will be a slight bias towards mood over genre and the user prefrences that have a higher weight rather than the ones on the lower end.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

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

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


# https://github.com/samanthapena507-arch/ai110-module3show-musicrecommendersimulation-starter.git
Implement recommender scoring/explanations and improve CLI-first simulation output
- Enhanced `recommend_songs` in `recommender.py` to return multiline, user-friendly explanations with a fallback when no strong matches are found
- Added concise one-line docstrings across recommender functions/methods for readability and maintainability
- Updated `main.py` console output to a clearer ranked format with score + reason breakdown per recommendation
- Added a richer sample preference profile for realistic CLI testing
- Result: the project now provides a working CLI-first music recommender simulation experience
