import streamlit as st
from sentiment import detect_mood
from spotify_api import get_songs_by_mood

# Page setup
st.set_page_config(page_title="🎧 Moodify – AI Song Recommender", layout="centered", page_icon="🎵")

# Style (Optional CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f4f6fa;
    }
    .stTextArea textarea {
        font-size: 1.1rem;
        border-radius: 8px;
    }
    .song-card {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# App header
st.title("🎧 Moodify – AI Song Recommender")
st.markdown("##### _Let your feelings pick your playlist_")

# Language selector
language = st.selectbox("🌐 Choose song language", ["Telugu", "Hindi", "English"], index=0)

# Mood input
user_input = st.text_area("🗨️ How are you feeling today?", placeholder="Type something like 'I’m feeling peaceful and relaxed'...")

# Main action
if st.button("🎵 Recommend Songs"):
    if user_input.strip():
        with st.spinner("🔍 Analyzing mood using AI..."):
            mood = detect_mood(user_input)
            songs = get_songs_by_mood(mood, language)

        st.markdown(f"### 🎯 Detected Mood: :blue[**{mood}**]")

        if songs:
            st.markdown("### 🎶 Your Recommendations:")
            for idx, song in enumerate(songs, 1):
                st.markdown(f"""
                    <div class="song-card">
                        <h4>{idx}. {song['name']}</h4>
                        <p><b>Artist:</b> {song['artist']}</p>
                        <a href="{song['url']}" target="_blank">▶️ Listen on Spotify</a>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No songs found for this mood. Try again or check your Spotify API keys.")
    else:
        st.warning("Please enter some text to analyze.")

# Footer
st.markdown("---")
st.markdown("Buit with ❤️ by Chintu")
