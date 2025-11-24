import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.7:
        return "joy"
    elif 0.2 <= compound < 0.7:
        return "happy"
    elif -0.2 < compound < 0.2:
        return "neutral"
    elif -0.7 < compound <= -0.2:
        return "sad"
    else:
        return "anger"
