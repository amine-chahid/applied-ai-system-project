from recommender import load_songs, recommend_songs
from evaluator import evaluate_results
from logger import log
from tabulate import tabulate

def main() -> None:
    # Load songs from CSV
    songs = load_songs("data/songs.csv")

    # Predefined user profiles
    profiles = {
        "High Energy Pop": {
            "favorite_genre": "pop",
            "preferred_mood": "happy",
            "energy_preference": 0.9,
            "valence_preference": 0.8,
            "danceability_preference": 0.9
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "preferred_mood": "chill",
            "energy_preference": 0.3,
            "valence_preference": 0.6,
            "danceability_preference": 0.5
        },
        "Intense Rock": {
            "favorite_genre": "rock",
            "preferred_mood": "intense",
            "energy_preference": 0.95,
            "valence_preference": 0.4,
            "danceability_preference": 0.7
        },
        "Edge Case (Conflicting)": {
            "favorite_genre": "lofi",
            "preferred_mood": "sad",
            "energy_preference": 0.9,
            "valence_preference": 0.2,
            "danceability_preference": 0.4
        }
    }

    # Loop through profiles
    for profile_name, user_prefs in profiles.items():
        print(f"\n==============================")
        print(f"Profile: {profile_name}")
        print(f"==============================\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        table = []

        for song, score, explanation in recommendations:
            table.append([
                song["title"],
                song["artist"],
                f"{score:.2f}",
                explanation
            ])

        # Display results
        print(tabulate(
            table,
            headers=["Title", "Artist", "Score", "Reasons"],
            tablefmt="grid"
        ))

        # ✅ Evaluation (REQUIRED)
        confidence = evaluate_results(recommendations)
        print(f"\nSystem Confidence: {confidence}")

        # ✅ Logging (REQUIRED)
        log(f"Profile: {profile_name}")
        log(f"User prefs: {user_prefs}")
        log(f"Recommendations: {recommendations}")
        log(f"Confidence: {confidence}")


if __name__ == "__main__":
    main()