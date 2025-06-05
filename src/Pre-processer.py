#Pre-processor
import pandas as pd
import re


# Load raw reviews
df = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analytics/data/raw_reviews.csv")

# Drop duplicates and NaNs
df.drop_duplicates(inplace=True)
df.dropna(subset=["content", "score"], inplace=True)


# Normalize dates
df['date'] = pd.to_datetime(df['at']).dt.date

def clean_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove special characters, URLs, emojis
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"[^a-zA-Z\s]", '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# Apply cleaning
df['cleaned_content'] = df['content'].apply(clean_text)  
#df.apply(clean_text)

# Save cleaned data
df.to_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analytics/data/clean_reviews.csv", index=False)
print("Cleaned reviews saved to data/clean_reviews.csv")






