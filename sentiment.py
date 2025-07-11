import openai
from textblob import TextBlob
from config import get_openai_key

def detect_mood(user_input):
    openai.api_key = get_openai_key()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a mood detector. Classify the user's message into one of these moods: Happy, Sad, Calm, Energetic, Romantic, Angry, Bored, Excited."
                },
                {"role": "user", "content": user_input}
            ]
        )
        mood = response['choices'][0]['message']['content'].strip()
        return mood
    except Exception:
        # Fallback to TextBlob if OpenAI fails
        polarity = TextBlob(user_input).sentiment.polarity
        if polarity > 0.5:
            return "Happy"
        elif polarity > 0.2:
            return "Calm"
        elif polarity < -0.5:
            return "Sad"
        elif polarity < 0:
            return "Bored"
        else:
            return "Neutral"
