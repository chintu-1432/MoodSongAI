import streamlit as st
from sentiment import detect_mood
from spotify_api import get_songs_by_mood

# ----- Streamlit Page Config -----
st.set_page_config(page_title="🎧 Moodify – AI Song Recommender", layout="centered", page_icon="🎵")

# ----- Custom CSS & Animations -----
st.markdown("""
<style>
/* Smooth animation on page load */
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}

body {
    background: linear-gradient(to right, #f8f9fa, #e9ecef);
    font-family: 'Segoe UI', sans-serif;
}

/* Title and section animation */
h1, h2, .stSelectbox, .stTextArea, .stButton, .song-card {
    animation: fadeInUp 0.6s ease-in-out;
}

/* Main app container */
.main {
    background-color: #f7f9fb;
}

/* Text area styling */
.stTextArea textarea {
    font-size: 1.05rem;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #ccc;
}

/* Song card */
.song-card {
    background: #ffffff;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.07);
    transition: 0.3s ease-in-out;
}
.song-card:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

/* Spotify link styling */
a.spotify-link {
    color: #1DB954;
    text-decoration: none;
    font-weight: bold;
}
a.spotify-link:hover {
    text-decoration: underline;
}

/* Styled buttons */
.stButton > button {
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    transition: background 0.3s ease;
}
.stButton > button:hover {
    background: linear-gradient(to right, #2575fc, #6a11cb);
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

# ----- App Title -----
st.title("🎧 Moodify – AI Song Recommender")
st.markdown("#### _Let your feelings choose your playlist._")

# ----- Language Selection -----
language = st.selectbox("🌐 Select language for song recommendations", ["Telugu", "Hindi", "English"])

# ----- Mood Input -----
user_input = st.text_area("🗨️ How are you feeling today?", placeholder="e.g., Feeling peaceful and happy...")

# ----- Generate Recommendations -----
if st.button("🎵 Recommend Songs"):
    if user_input.strip():
        with st.spinner("Analyzing mood using AI..."):
            mood = detect_mood(user_input)
            songs = get_songs_by_mood(mood, language)

        st.markdown(f"### 🧠 Detected Mood: **:blue[{mood}]**")

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

# ----- Footer -----
st.markdown("---")
st.markdown("<footer>Made with ❤️ using OpenAI, Spotify API & Streamlit</footer>", unsafe_allow_html=True)
