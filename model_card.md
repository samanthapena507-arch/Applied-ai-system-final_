# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name   

Model Name: SongScavenger 2.0
---

## 2. Limitations and Biases of the System

One of the limitations of the SongScavenger 2.0 model is the song catalogue it has access to. As the AI in the system cannot understand the lyrics of the songs it recommends there could be songs that are not suited to certain age groups. To help negate this problem the system can only pull recommendations from the songs.csv file which can then be manually controlled and manipulated based on the age range of the user and other restrictions they may have. The system has biases when it come to more pop music leaning users as the results will be more accurate to the users tastes compared to other genres. This bias comes from the data the system is given as it is small and has a more pop songs than any other genre. This is a bias that can be fixed through diversification and a larger data set, however, it may affect the programs runtime. The larger the data set the slower the program may run as it must first load the songs from the data set provided and then find the top songs by ranking them.

---

## 3. AI Misuse and Prevention

I am of the belief that any AI can be misused no matter the range of the system because it is harder to account for the different ways a user could manipulate it. With this system in particular I think the way that it can be misused the most is to recommend songs that are not appropriate for some people. Since the AI can also be a learning model there is the potential for a user to try and boost some songs over others by constantly putting in keywords that would trigger a certain song to rank high consistently. The prevention for the first misuse is the limitation of the dataset. The dataset that the system is allowed to grab from is also able to be edited to take songs out or put them in based on what would better fit the restrictions of each user or future user. This prevention measure is something that can be fixed upon further work on the program. For the second misuse as it is more of a theoretical misuse there is not yet a fix that can be readily implemented aside from human lead bias checks.

---

## 4. Surprises with Reliability 

What surprised me the most in testing the systems reliability was when I put in no keywords for the system to use. The results of this test surprised me as I was not sure if the system would be able to handle that specific edge case well. In the end it was able to give a clean and semi-helpful result that it deemed neutral and balanced. This, however, did prove its reliability in that regard as well as through other tests to get specific or mixed results based on the keywords used. The use of the keywords were also surprising in a way as even using keywords that are not in the original dataset were handled well and incorporated in the results.

---

## 5. AI Collaboration

My collaboration with the AI in this project was a mix of Copilot and Claude since I wanted to make sure that I would have enough credits in both. I used the AI mainly for wiring in the Gemini API as I was unfamiliar with that part of the coding process. I also used the systems to give me a starting off point as I was having trouble seeing the full picture of the project at hand. It was during this part of my AI collaboration that I seemed to run into a few bumps as it seemed at time that the AI was overcomplicating the problem. I would ask it to help me with figuring out first steps and it would start giving me a list of obscure and high level programming processes and jargon. It was at this time that I realized I needed to step back and re-evaluate what the best course of action would be for me and my current skill level. The AI was helpful when I was having trouble getting the Gemini API fully integrated into the system and when it helped me upgrade from console output only to both console and UI output making my final project look much nicer and clean.

--- 
