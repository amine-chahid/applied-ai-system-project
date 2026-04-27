# 🎧 Model Card: Applied AI Music Recommendation System

## 1. Model Name  

Applied AI Music Recommender v1.0  

---

## 2. Goal / Task  

The goal of this system is to recommend songs based on a user’s preferences.  

It suggests songs that match the user’s genre, mood, and audio features, while also demonstrating how an AI system can retrieve, rank, and evaluate results.

---

## 3. Data Used  

The system uses a dataset of songs stored in `songs.csv`.

Each song includes:
- Genre  
- Mood  
- Energy  
- Tempo  
- Valence  
- Danceability  
- Acousticness  

The dataset contains a mix of genres such as pop, lofi, rock, and ambient.  
However, it is small and does not represent all types of music.

---

## 4. How the System Works  

The system works in three main stages:

### 1. Retrieval (RAG)
The system first filters songs based on the user’s preferred mood.  
This step reduces irrelevant options and improves recommendation quality.

### 2. Recommendation (Scoring)
Each song is scored based on:

- Genre match (+2.0)  
- Mood match (+1.5)  
- Energy similarity  
- Valence similarity  
- Danceability similarity  

Songs closer to the user’s preferences receive higher scores.

### 3. Evaluation
The system assigns a confidence score:

- 0.9 → strong recommendations  
- 0.3 → weak or missing results  

---

## 5. Strengths  

- Produces clear and explainable recommendations  
- Retrieval step improves relevance  
- Handles multiple user profiles effectively  
- Simple and interpretable logic  

---

## 6. Limitations and Bias  

- Small dataset limits diversity  
- Strong bias toward matching genre  
- Retrieval only uses mood  
- Does not learn from user feedback  

During testing, genre had a stronger influence than mood, which reduced variety in some cases.

---

## 7. Evaluation Process  

The system was tested using multiple user profiles:

- High Energy Pop  
- Chill Lofi  
- Intense Rock  
- Edge Case (conflicting preferences)  

Results:
- All profiles returned valid recommendations  
- Confidence scores were consistently high (0.9)  
- Edge cases revealed bias toward genre  

---

## 8. Intended Use and Non-Intended Use  

**Intended Use:**
- Educational demonstration of AI systems  
- Understanding recommendation systems  

**Non-Intended Use:**
- Real-world production systems  
- Large-scale music recommendation  

---

## 9. Future Improvements  

- Expand dataset for more diversity  
- Improve retrieval using multiple features  
- Add machine learning-based ranking  
- Incorporate user feedback  

---

## 10. Personal Reflection  

This project showed me that AI systems are not just about generating outputs, but also about reliability, explainability, and trust.

Adding retrieval, evaluation, and logging made the system behave more like a real-world AI application.