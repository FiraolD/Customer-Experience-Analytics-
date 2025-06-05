import pandas as pd
from textblob import TextBlob

df = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analytics/data/raw_reviews.csv")
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
df.to_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analytics/data/sentiment_reviews2.csv", index=False)
print("Sentiment analysis completed and saved.")