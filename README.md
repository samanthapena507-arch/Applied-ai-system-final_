# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Three things that are used when picking songs: likes, dislikes, and subscriptions/artist follows. Also a mix of content based filtering and collaborative 

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
The Extra user profiles and their outputs:
- 1. user_prefs2 = {"genre": "indie pop", "mood": "happy", "energy": 0.76, "tempo_bpm": 124, "valence": 0.81, "danceability": 0.82, "acousticness": 0.35}
=========================================================
Top recommendations:

#1 Rooftop Lights
Final Score: 4.00
Reasons:
  - genre match (+1.00)
  - mood match (+2.00)
  - energy similarity 1.00 (+0.30)
  - tempo_bpm similarity 1.00 (+0.25)
  - valence similarity 1.00 (+0.20)
  - danceability similarity 1.00 (+0.15)
  - acousticness similarity 1.00 (+0.10)
--------------------------------------------------
#2 Golden Hour Drift
Final Score: 3.96
Reasons:
  - genre match (+1.00)
  - mood match (+2.00)
  - energy similarity 0.95 (+0.28)
  - tempo_bpm similarity 0.98 (+0.25)
  - valence similarity 0.98 (+0.20)
  - danceability similarity 0.98 (+0.15)
  - acousticness similarity 0.89 (+0.09)
--------------------------------------------------
#3 Sunrise City
Final Score: 2.94
Reasons:
  - mood match (+2.00)
  - energy similarity 0.94 (+0.28)
  - tempo_bpm similarity 0.95 (+0.24)
  - valence similarity 0.97 (+0.19)
  - danceability similarity 0.97 (+0.15)
  - acousticness similarity 0.83 (+0.08)
--------------------------------------------------
#4 Gym Hero
Final Score: 0.89
Reasons:
  - energy similarity 0.83 (+0.25)
  - tempo_bpm similarity 0.93 (+0.23)
  - valence similarity 0.96 (+0.19)
  - danceability similarity 0.94 (+0.14)
  - acousticness similarity 0.70 (+0.07)
--------------------------------------------------
#5 Afterglow Avenue
Final Score: 0.89
Reasons:
  - energy similarity 0.97 (+0.29)
  - tempo_bpm similarity 0.92 (+0.23)
  - valence similarity 0.70 (+0.14)
  - danceability similarity 0.94 (+0.14)
  - acousticness similarity 0.84 (+0.08)
--------------------------------------------------
=========================================================
=========================================================
- 2. user_prefs3 = {"genre": "lofi", "mood": "focused", "energy": 0.5, "tempo": 80, "valence": 0.65}
=========================================================
Top recommendations:

#1 Focus Flow
Final Score: 3.71
Reasons:
  - genre match (+1.00)
  - mood match (+2.00)
  - energy similarity 0.90 (+0.27)
  - tempo_bpm similarity 1.00 (+0.25)
  - valence similarity 0.94 (+0.19)
--------------------------------------------------
#2 Glass Horizon
Final Score: 2.62
Reasons:
  - mood match (+2.00)
  - energy similarity 0.75 (+0.22)
  - tempo_bpm similarity 0.85 (+0.21)
  - valence similarity 0.93 (+0.19)
--------------------------------------------------
#3 Midnight Coding
Final Score: 1.70
Reasons:
  - genre match (+1.00)
  - energy similarity 0.92 (+0.28)
  - tempo_bpm similarity 0.98 (+0.25)
  - valence similarity 0.91 (+0.18)
--------------------------------------------------
#4 Library Rain
Final Score: 1.68
Reasons:
  - genre match (+1.00)
  - energy similarity 0.85 (+0.26)
  - tempo_bpm similarity 0.93 (+0.23)
  - valence similarity 0.95 (+0.19)
--------------------------------------------------
#5 Quiet Hands
Final Score: 0.68
Reasons:
  - energy similarity 0.83 (+0.25)
  - tempo_bpm similarity 0.93 (+0.23)
  - valence similarity 0.98 (+0.20)
--------------------------------------------------
=========================================================
=========================================================
- 3. user_prefs4 = {"genre": "metal", "mood": "chill", "energy": 0.65, "tempo_bpm": 125, "valance": 0.8, "danceability": 0.7, "acoustic": 0.4}
=========================================================
Top recommendations:

#1 Midnight Coding
Final Score: 2.74
Reasons:
  - mood match (+2.00)
  - energy similarity 0.77 (+0.23)
  - tempo_bpm similarity 0.61 (+0.15)
  - valence similarity 0.76 (+0.15)
  - danceability similarity 0.92 (+0.14)
  - acousticness similarity 0.69 (+0.07)
--------------------------------------------------
#2 Library Rain
Final Score: 2.70
Reasons:
  - mood match (+2.00)
  - energy similarity 0.70 (+0.21)
  - tempo_bpm similarity 0.56 (+0.14)
  - valence similarity 0.80 (+0.16)
  - danceability similarity 0.88 (+0.13)
  - acousticness similarity 0.54 (+0.05)
--------------------------------------------------
#3 Window Seat Weather
Final Score: 2.69
Reasons:
  - mood match (+2.00)
  - energy similarity 0.64 (+0.19)
  - tempo_bpm similarity 0.59 (+0.15)
  - valence similarity 0.93 (+0.19)
  - danceability similarity 0.79 (+0.12)
  - acousticness similarity 0.47 (+0.05)
--------------------------------------------------
#4 Spacewalk Thoughts
Final Score: 2.63
Reasons:
  - mood match (+2.00)
  - energy similarity 0.63 (+0.19)
  - tempo_bpm similarity 0.46 (+0.11)
  - valence similarity 0.85 (+0.17)
  - danceability similarity 0.71 (+0.11)
  - acousticness similarity 0.48 (+0.05)
--------------------------------------------------
#5 Thunder Bloom
Final Score: 1.70
Reasons:
  - genre match (+1.00)
  - energy similarity 0.67 (+0.20)
  - tempo_bpm similarity 0.68 (+0.17)
  - valence similarity 0.59 (+0.12)
  - danceability similarity 0.98 (+0.15)
  - acousticness similarity 0.64 (+0.06)
--------------------------------------------------
=========================================================

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
When I changed the weight for the genre and energy in my program the results were surprisingly similar but there were still a few differences in the recommended songs but I wouldn't say that the change made the recommendations all that more accurate.
- What happened when you added tempo or valence to the score
I think when the system has more guides to follow it helps to make the recommendatons more accurate as it has a clearer picture of what the user wants.
- How did your system behave for different types of users
Due to the lack of a heirarchy the program behaved more consistantly with profiles that better matched the majority of the songs in the data set and had a harder time with profiles that might have been similar but didn't directly match the mood or genre of a song.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

I think the recommender would work better with a bigger catalog accuracy wise, however, that doesn't take into account the extra time it will take the program to execute. There is also the issue that comes with general message and content of the song as though it might match the users prefrences in respect to the songs components but the lyrics could be inappropriate or offensive to the user. When it comes to favor it seems to favor the happy mooded pop loving users as oppsed to those who favor metal.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

What I learned about how recommenders turn data into predictions starts with the number of things the program has to consider since the ones covered in this project are not the end all be all. It also makes me think more about how we gave the program the data it needed directly where the recommender systems in apps like spotify have to gather most of that information indirectly. Those systems get the information from the songs and artists we interact with and then process and find the most common aspects of songs that the user likes. There is also prefrences like the level of lyricism a song has as well as the laguges the user likes as a user can like songs in many different languages. I think the biases that can come up can be in language for one but also the message portrayed in the song, and even with the artists they feature. Though I doubt it would happen with bigger platforms data set bias when it comes to song diversity can also be a problem that comes up.

Moving on to the use of my AI tools it helped me the most with getting a started on the ranking logic and how things could be organized. This was great because it was not something I had experience thinking about often in such detail. There were times when it gave me ideas that I didn't think were great namely when it talked about the distribution of points since it felt like it made the point system overly complicated. Going through and planning it helped me realize how something like a recommendation can seem simple but as you go further into the actual process you can see the underlying intricacies of the algorithm. If I were to develop the project more I think I would clean up the output a little more and either try to bring it out of the terminal or try to use real song data to make it work more for the real world.
