import json
import boto3

# Initialize the Amazon Comprehend client
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    # Extract the review text from the event
    review_text = event['review']

    # Use Amazon Comprehend to detect the sentiment
    response = comprehend.detect_sentiment(Text=review_text, LanguageCode='en')

    # Get the sentiment (e.g., POSITIVE, NEGATIVE, NEUTRAL, MIXED)
    sentiment = response['Sentiment']

    # Log the sentiment result
    print(f"Review: {review_text}")
    print(f"Sentiment: {sentiment}")

    # Return the sentiment result as a response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'review': review_text,
            'sentiment': sentiment
        })
    }
