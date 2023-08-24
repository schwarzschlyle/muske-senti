import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def handler(event, context):
    data = json.loads(event['body'])
    text = data['text']

    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)

    response = {
        "statusCode": 200,
        "body": json.dumps(sentiment)
    }

    return response
