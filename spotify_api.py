import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import get_spotify_credentials

def get_songs_by_mood(mood, language="Telugu"):
    client_id, client_secret = get_spotify_credentials()
    auth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth)

    # Add language-specific query for each mood
    mood_query_map = {
        "Happy": f"happy {language} songs",
        "Sad": f"sad {language} songs",
        "Calm": f"calm {language} acoustic",
        "Energetic": f"{language} energetic dance hits",
        "Romantic": f"romantic {language} songs",
        "Angry": f"{language} intense rock",
        "Bored": f"{language} lofi chill",
        "Excited": f"{language} party hits",
        "Neutral": f"{language} hits"
    }

    query = mood_query_map.get(mood, f"{language} songs")

    try:
        results = sp.search(q=query, type="track", limit=10)
        songs = []

        for item in results['tracks']['items']:
            songs.append({
                "name": item['name'],
                "artist": item['artists'][0]['name'],
                "url": item['external_urls']['spotify']
            })

        return songs
    except Exception as e:
        print("Error fetching songs:", e)
        return []
