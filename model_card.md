# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Model Name: SongScavenger 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
SongScavenger recommends songs for thier users based on the users prefrences in songs structure as well as mood and genre.
- What assumptions does it make about the user  
Tje model assumes that the user puts in the song elements they input as well as that the user knows the range and sticks to it.
- Is this for real users or classroom exploration  
I think though the recommender is functional it is more for classroom exploration as there is no current heirarchy in place for things like mood and genre and it takes in raw song stats in a certain format. If the song information is not formatted correctly the program won't be able to load the songs for processing.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
The way that scoring is set up you can use some or all of the available song components that are present in the songs.csv file 
- What user preferences are considered  
The prefrences that are considered most are the prefered mood and genre of the user otherwise things like prefered energy, tempo, valence, danceability, and acousticness in decending weights.
- How does the model turn those into a score 
each song has a score that starts off as zero and then gains 1 point for a matching genre and 2 for a matching mood. The program then goes on to calculate the distance of the numerical stats from the users set prefrences, applies their respective weights and then adds the rewarded amount of points to the overall song total. 
- What changes did you make from the starter logic  
I included room for certain aliases for when the user is adding their prefrences to make up for slight case discrepancies 

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog 
There are currently 18 songs in the song catalog 
- What genres or moods are represented  
genres: pop, indie pop, lofi, rock, ambient, jazz, metal, synthwave, hip-hop, folk, and acoustic
moods: happy, chill, intense, relaxed, moody, focused, and confident
- Did you add or remove data  
I added 8 songs to the data set after the first 10 default songs
- Are there parts of musical taste missing in the dataset  
I think there could be some more genres like classical, R&B, country, and alternative as well as more moods since the current list is shorter than the number of genres

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
The systems seem to work best with the pop genres and those who enjoy happy music as it can better find songs that match those attributes in the current data set
- Any patterns you think your scoring captures correctly  
I think the program is good at finding the best songs when there are consistent prefrences and there are many matches. it starts to be less acurate when it has to rely more on the numerical components since they don't account for what kind of song they are
- Cases where the recommendations matched your intuition  
When I put in my own prefrences of a happy indie pop music taste as well as the focused lofi music taste were pretty accurate and gave me the output I was expecting as well as the one I put in to match an existing song in the data set
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
one feature the program does not consider is when the user enters number outside the set range. when this happens the score for that feature is automatically put to zero.
- Genres or moods that are underrepresented  
Since the system uses exact-string matching it can exclude valid prefrences or not give partial credit for a when a genre is indie pop and not pop for example. Without a heirarchy to give partial points there can be genre of moods that go underrepresented.
- Cases where the system overfits to one preference  
Since the bonous points for matching genre and mood are higher than the other number based song components the system can be biased towards songs with same genre and mood but different number based components. 
- Ways the scoring might unintentionally favor some users 
If the users favorite genre and/or mood is the same as the most common mood and/or genre in the data set that user will get more tailored recommendations as opposed to one who favors heavy metal intense music for example. 

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
The first random profile that i tested was a lofi focused kind of profile. This one had results that seemed pretty accurate as the songs were other lofi more chill songs.

The second was a chill metal profile to test conflicting types. This one was probably the most out there as recommendations come since the genre and mood were in conflict with each other. infact it was actually close to the focused lofi profile since the mood was the main thing giving points to the top songs.

The third was a happy indie pop profile based after my prefrences. compared to the other tests outputs the results are pretty different since the genre and moods are not as very similar. 
- What you looked for in the recommendations  
In the recommendations I looked at the genre and mood of the recommended songs to see if they made sense for what was input by the user then I went to the numerical values to see how similar they were and if the difference was acceptable.
- What surprised you  
I was surprised by the recommendations for the chill metal profile as it gave some songs that were in the top five recommended for the focused lofi profile. This was likely due to the bias towards mood over genre and the diversity of the data set since metal was one of the least represented genres. Not to mention that again the mood and genre of the profile do not match what is typically seen in music.
- Any simple tests or comparisons you ran  
The first sample test I did was to see if the recommender would pick the song I wanted as the top song. I made the profile tailored to the specific song and it did in fact make it the top song. Other tests were done to test the aliases for some of the numerical inputs as well as conflicting genres and moods as mentioned above. 

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences 
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

When looking to improve the model I would first put in a heirarchy for the genres and moods so that partial bonuses can be added. This would help make the system more useable and accurate. I think I would also try to simplify the explanations to show just the points earned or a percentage of how simmilar the song is to the users prefrences. When it comes to improving the diversity among the resluts the best I can think of is to simply increase the size and diversity of the data set that the program is given that way it can have more songs to pick from that could be better matches. another could also be tweaking the tie-breaker policy to something based on the song components rather than input order. Then for handling complex or conflicting user tatses I would probably expand the genre and mood categories to have secondary or tertiary mood and genre prefrences so the system has more to work with when it comes to the general vibe of the song.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

From this I learned to think more about the details of the program before getting into the code which is something I struggle with. What I learned of the systems them selves was how much data diversity and song components play a part in the accuracy of song recommendations. It also makes me more aware of why many apps that ask you about your prefrences before looking at the content they show you. They need a rough set of data to start with when creating your user profile so they can show you preliminary recommendations. 
