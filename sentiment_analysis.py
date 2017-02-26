from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
def get_sentiment_score(text):
    sa = sid.polarity_scores(text)
    return sa['compound']

def get_sentiment(text):
    score = get_sentiment_score(text)

    return -1 if score < -0.1 else 1 if score > 0.2 else 0