🎵 Hindi Song Recommendation System
A Python-based music recommendation system that suggests Hindi songs based on a song name, mood, or lyric using multilingual sentence embeddings and cosine similarity.

✨ Features

🎶 Recommends Hindi songs by song name, mood, or lyric snippet
🌐 Multilingual support — understands both Hindi and English input
🧠 Powered by paraphrase-multilingual-MiniLM-L12-v2 sentence embeddings
⚡ Fast similarity search using cosine similarity
📁 Works with a simple CSV dataset


🛠 Tech Stack
Layer       Technology 
Language    Python 3.x
Data        Pandas
Embeddings  Sentence Transformers (paraphrase-multilingual-MiniLM-L12-v2)
Similarity  Scikit-learn (Cosine Similarity)

⚙️ How It Works

Loads a CSV dataset containing song title, artist, and mood
Combines these fields into a single text representation per song
Encodes all songs into vector embeddings using a multilingual transformer model
Takes user input (song name / mood / lyric)
Encodes the query and computes cosine similarity against all song embeddings
Returns the top-N most similar songs


🚀 Getting Started
Prerequisites

Python 3.8 or higher
pip

Installation

Clone the repository

bashgit clone https://github.com/Charu041203/hindi-song-recommendation.git
cd hindi-song-recommendation

Create a virtual environment (recommended)

bashpython -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

Install dependencies

bashpip install pandas scikit-learn sentence-transformers

Add your dataset — Place a songs.csv file in the project root with these columns:

ColumnDescriptiontitleSong titleartistSinger / Band namemoodMood tag (e.g. Romantic, Sad, Party)
Usage
bashpython hindisongs.py
=== Hindi Song Recommendation System ===

Enter a song name / mood / lyric: Tum Hi Ho

Finding recommendations...

Tum Hi Ho — Arijit Singh  (Mood: Romantic)
Tera Ban Jaunga — Akhil Sachdeva  (Mood: Romantic)
Channa Mereya — Arijit Singh  (Mood: Sad)
Phir Bhi Tumko Chahungo — Arjit Singh  (Mood: Romantic)
Ae Dil Hai Mushkil — Arijit Singh  (Mood: Sad)
