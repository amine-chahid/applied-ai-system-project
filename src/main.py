from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "favorite_genre": "pop",
        "preferred_mood": "happy",
        "energy_preference": 0.8,
        "valence_preference": 0.7,
        "danceability_preference": 0.8
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}\n")


if __name__ == "__main__":
    main()