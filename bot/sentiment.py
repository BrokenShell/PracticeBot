from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()


def sentiment_score(text: str) -> float:
    return vader.polarity_scores(text)["compound"]
