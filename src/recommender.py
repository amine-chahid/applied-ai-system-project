from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


# =========================
# DATA CLASSES
# =========================

@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


# =========================
# OOP RECOMMENDER
# =========================

class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []

        for song in self.songs:
            score = 0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.5

            # Energy similarity (bounded)
            energy_score = max(0, 1 - abs(song.energy - user.target_energy))
            score += energy_score

            if user.likes_acoustic:
                score += song.acousticness

            scored.append((song, score))

        scored.sort(key=lambda x: x[1], reverse=True)

        return [s[0] for s in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("matches favorite genre")

        if song.mood == user.favorite_mood:
            reasons.append("matches preferred mood")

        energy_diff = abs(song.energy - user.target_energy)
        reasons.append(f"energy difference: {energy_diff:.2f}")

        if user.likes_acoustic:
            reasons.append("user prefers acoustic music")

        return ", ".join(reasons)


# =========================
# LOAD SONGS (CSV)
# =========================

def load_songs(csv_path: str) -> List[Dict]:
    songs = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


# =========================
# FUNCTIONAL RECOMMENDER
# =========================
from retriever import retrieve_songs_by_mood

def recommend_songs(user_prefs, songs, k=5):

    # 🔥 RAG STEP (retrieve first)
    filtered_songs = retrieve_songs_by_mood(songs, user_prefs["preferred_mood"])

    # fallback if no match
    if not filtered_songs:
        filtered_songs = songs

    results = []

    for song in filtered_songs:
        score = 0
        reasons = []

        # Genre
        if song["genre"] == user_prefs["favorite_genre"]:
            score += 2.0
            reasons.append("genre match (+2.0)")

        # Mood
        if song["mood"] == user_prefs["preferred_mood"]:
            score += 1.5
            reasons.append("mood match (+1.5)")

        # Energy
        energy_score = max(0, 1 - abs(song["energy"] - user_prefs["energy_preference"]))
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")

        # Valence
        valence_score = max(0, 1 - abs(song["valence"] - user_prefs["valence_preference"]))
        score += valence_score
        reasons.append(f"valence similarity (+{valence_score:.2f})")

        # Danceability
        dance_score = max(0, 1 - abs(song["danceability"] - user_prefs["danceability_preference"]))
        score += dance_score
        reasons.append(f"danceability similarity (+{dance_score:.2f})")

        explanation = ", ".join(reasons)

        results.append((song, score, explanation))

    results = sorted(results, key=lambda x: x[1], reverse=True)

    return results[:k]