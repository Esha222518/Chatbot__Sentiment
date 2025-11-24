import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon (only the first time)
nltk.download('vader_lexicon', quiet=True)

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str):
    """
    Analyzes sentiment of the input text.

    Returns:
        label (str): 'Positive', 'Negative', or 'Neutral'
        scores (dict): Dictionary of VADER sentiment scores
    """
    # Get VADER scores
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    # Determine sentiment label based on compound score
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'

    # Return both label and scores
    return label, scores
