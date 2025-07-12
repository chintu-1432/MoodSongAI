import streamlit as st
from sentiment import detect_mood
from spotify_api import get_songs_by_mood

# Streamlit Page Config
st.set_page_config(page_title="🎧 Moodify – AI Song Recommender", layout="centered", page_icon="🎵")

# ----- Custom Dark Mode CSS -----
st.markdown("""
<style>
/* Full dark background */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #121212;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

/* Animate content */
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}
h1, h2, .stSelectbox, .stTextArea, .stButton, .song-card {
    animation: fadeInUp 0.6s ease-in-out;
}

/* Input textarea */
.stTextArea textarea {
    font-size: 1.05rem;
    padding: 1rem;
    border-radius: 10px;
    background-color: #1e1e1e;
    color: #fff;
    border: 1px solid #333;
}

/* Song card */
.song-card {
    background: #1e1e1e;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.song-card:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 24px rgba(255, 255, 255, 0.1);
}

/* Spotify link */
a.spotify-link {
    color: #1DB954;
    text-decoration: none;
    font-weight: bold;
}
a.spotify-link:hover {
    text-decoration: underline;
}

/* Dark glowing button */
.stButton > button {
    background: linear-gradient(to right, #43cea2, #185a9d);
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    transition: 0.3s ease;
    box-shadow: 0 0 10px rgba(66, 245, 188, 0.3);
}
.stButton > button:hover {
    background: linear-gradient(to right, #185a9d, #43cea2);
    box-shadow: 0 0 20px rgba(66, 245, 188, 0.5);
}

/* Footer */
footer {
    text-align: center;
    font-size: 0.85rem;
    color: #888;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎧 Moodify – AI Song Recommender")
st.markdown("#### _Let your feelings choose your playlist._")

# Language dropdown
language = st.selectbox("🌐 Select language for song recommendations", ["Telugu", "Hindi", "English"])

# Mood text input
user_input = st.text_area("🗨️ How are you feeling today?", placeholder="e.g., Feeling peaceful and happy...")

# Button action
if st.button("🎵 Recommend Songs"):
    if user_input.strip():
        with st.spinner("Analyzing mood using AI..."):
            mood = detect_mood(user_input)
            songs = get_songs_by_mood(mood, language)

        st.markdown(f"### 🧠 Detected Mood: **:green[{mood}]**")

        if songs:
            st.markdown("### 🎶 Your Playlist:")
            for idx, song in enumerate(songs, 1):
                st.markdown(f"""
                <div class="song-card">
                    <h4>{idx}. {song['name']}</h4>
                    <p>🎤 Artist: <strong>{song['artist']}</strong></p>
                    <p><a class="spotify-link" href="{song['url']}" target="_blank">▶️ Listen on Spotify</a></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No songs found for this mood. Try again later.")
    else:
        st.warning("Please describe your mood before clicking.")

# Footer
st.markdown("---")
st.markdown("<footer>Built with ❤️ by Chintu</footer>", unsafe_allow_html=True)
