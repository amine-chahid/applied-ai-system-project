# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch Recommender 1.0
---

## 2. Intended Use  

This recommender system is designed to suggest songs based on a user’s musical preferences. It generates recommendations by comparing song features like genre, mood, and energy with the user’s taste profile.

The system assumes that a user has consistent preferences (for example, liking a certain genre or mood). It is built for classroom exploration and learning purposes, not for real-world deployment. Its goal is to demonstrate how recommendation systems transform user data into suggestions 

---

## 3. How the Model Works  

The model uses a content-based approach. It compares each song’s attributes with the user’s preferences and assigns a score based on similarity.

It considers:

Genre (exact match)
Mood (exact match)
Energy (how close the values are)
Valence (how positive or happy the song feels)
Danceability (how suitable the song is for movement)

Songs receive higher scores when they closely match the user’s preferences. Exact matches (like genre or mood) are weighted more heavily, while numerical features are scored based on how close they are to the user’s target values.

Compared to the starter logic, I expanded the system by adding more features (valence and danceability) and improved the scoring to better capture the overall “vibe” of a song instead of relying only on simple matches.

---

## 4. Data  

The dataset contains 10 songs with attributes such as:

Genre
Mood
Energy
Tempo
Valence
Danceability
Acousticness

The songs cover a mix of genres including pop, lofi, rock, ambient, jazz, synthwave, and indie pop.

Although the dataset includes some variety, it is still small and does not fully represent all musical tastes. It also does not include features like lyrics, language, or artist popularity.  

---

## 5. Strengths  

The system works well for users with clear and consistent preferences, such as someone who enjoys a specific genre and mood.

It captures the “vibe” of music effectively by combining multiple features instead of relying on just one. In many cases, the top recommendations matched my expectations, especially when testing profiles like “pop/happy” or “lofi/chill.”

Another strength is that the system provides explanations for each recommendation, making it easy to understand why a song was suggested.

---

## 6. Limitations and Bias 

The system has several limitations.

It strongly favors songs that match the selected genre, which means it may ignore good recommendations from other genres. This can create a “filter bubble” where users only see similar types of music.

The dataset is small and may not represent all genres or moods equally, which can bias the results. The model also assumes that all users have simple, fixed preferences, which is not realistic.

Additionally, the system does not consider important factors like user history, context, or changing tastes over time.  

---

## 7. Evaluation  

I tested the system using different user profiles, such as:

Pop / happy / high energy
Lofi / chill / low energy

I evaluated whether the top recommended songs matched the expected vibe. In most cases, the system performed well and selected songs that aligned with the user’s preferences.

One interesting observation was that even when genre did not match, songs with similar energy and mood still ranked relatively high, showing that the numerical features were working as intended

---

## 8. Future Work  

If I had more time, I would improve the system by:

Adding more songs to increase diversity
Including more features like lyrics or artist similarity
Introducing collaborative filtering using other users’ data
Improving diversity so recommendations are not too similar
Making the system adapt to changing user preferences

---

## 9. Personal Reflection  

This project helped me understand how recommendation systems convert user preferences into numerical scores and rankings. I learned that even simple rules can produce useful recommendations, but small design choices (like feature weights) can have a big impact.

One interesting takeaway was how easily bias can appear, especially when the system prioritizes one feature like genre. It made me realize that real-world systems must balance personalization with diversity.

Overall, this project gave me a much clearer understanding of how apps like Spotify and YouTube recommend content, and it showed me that human judgment is still important in designing fair and useful systems.
