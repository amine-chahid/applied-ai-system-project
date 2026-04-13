from tabulate import tabulate
from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

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

        print(tabulate(
            table,
            headers=["Title", "Artist", "Score", "Reasons"],
            tablefmt="grid"
        ))


if __name__ == "__main__":
    main()