🎵 Hindi Song Recommendation System
📌 Project Overview

This project is a Hindi Song Recommendation System that suggests songs based on user input such as:

Song name
Mood
Lyrics

It uses Natural Language Processing (NLP) and Sentence Transformers to find semantically similar songs and recommend the most relevant ones.

🚀 Features
🔍 Search songs using text input (name, mood, or lyrics)
🤖 Uses SentenceTransformer (MiniLM model) for semantic understanding
📊 Computes similarity using cosine similarity
🎯 Returns Top-N relevant song recommendations
🌐 Supports multilingual inputs (Hindi + English)
🛠️ Technologies Used
Python 🐍
Pandas 📊
Sentence Transformers 🤖
Scikit-learn 📉
📂 Project Structure
📁 Hindi-Song-Recommender
│── hindisongs.py        # Main recommendation script
│── songs.csv            # Dataset (songs info)
│── README.md            # Project documentation
📊 Dataset

The dataset (songs.csv) should contain the following columns:

Column	Description
title	Song name
artist	Singer/Artist
mood	Mood of the song
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/hindi-song-recommender.git
cd hindi-song-recommender
2️⃣ Install dependencies
pip install pandas scikit-learn sentence-transformers
3️⃣ Run the project
python hindisongs.py
💡 How It Works

Combines song features:

title + artist + mood
Converts text into vector embeddings using transformer model
Takes user input and converts it into embedding
Computes cosine similarity between input and songs
Returns Top matching songs
🧠 Model Used
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
Lightweight and fast
Supports multiple languages
Good for semantic similarity tasks
📌 Example Usage
=== Hindi Song Recommendation System ===

Enter a song name / mood / lyric: romantic sad love

Finding recommendations...

Tum Hi Ho — Arijit Singh (Mood: Sad)
Raabta — Arijit Singh (Mood: Romantic)
...
🔮 Future Improvements
🎧 Add Spotify/YouTube API integration
🌟 Build a web app using React + Flask
❤️ Add user personalization
📱 Deploy as mobile app
