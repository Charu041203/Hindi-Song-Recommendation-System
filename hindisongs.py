import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("songs.csv")
df["combined"] = df["title"] + " " + df["artist"] + " " + df["mood"]
print("Loading model... (takes a few seconds)")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
print("Encoding songs...")
song_embeddings = model.encode(df["combined"].tolist())
def recommend_songs(input_text, top_n=5):
    print("\nFinding recommendations...\n")

    # Encode user query
    query_embedding = model.encode([input_text])

    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, song_embeddings)[0]

    # Get top-N indices
    top_idx = similarities.argsort()[::-1][:top_n]

    # Display results
    for i in top_idx:
        print(f"{df.loc[i, 'title']} — {df.loc[i, 'artist']}  (Mood: {df.loc[i, 'mood']})")
if __name__ == "__main__":
    print("\n=== Hindi Song Recommendation System ===")
    user_input = input("\nEnter a song name / mood / lyric: ")

    recommend_songs(user_input)
