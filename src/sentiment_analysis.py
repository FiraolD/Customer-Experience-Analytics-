from textblob import TextBlob

# Function to calculate sentiment
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

# Apply sentiment analysis
df['sentiment'] = df['content'].apply(get_sentiment)

# Save results
df.to_csv("data/sentiment_reviews.csv", index=False)
print("Sentiment analysis completed and saved.")