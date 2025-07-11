import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_key():
    return os.getenv("OPENAI_API_KEY")

def get_spotify_credentials():
    return os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")
