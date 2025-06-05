#Pre-processor
import pandas as pd
import re
#import nltk
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#from nltk.stem import WordNetLemmatizer
#nltk.download('stopwords', quiet=True)
#nltk.download('punkt',  quiet=True)
#nltk.download('wordnet',  quiet=True)

# Initialize lemmatizer (kept as is)
#lemmatizer = WordNetLemmatizer()

# Load raw reviews
df = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analytics/data/raw_reviews.csv")

# Drop duplicates and NaNs
df.drop_duplicates(inplace=True)
df.dropna(subset=["content", "score"], inplace=True)
# Initialize
#stop_words = set(stopwords.words('english'))
#lemmatizer = WordNetLemmatizer()


# Normalize dates
df['date'] = pd.to_datetime(df['at']).dt.date

def clean_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove special characters, URLs, emojis
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"[^a-zA-Z\s]", '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # Tokenize
    #tokens = word_tokenize(text)

    # Remove stopwords and lemmatize
    #cleaned = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords]

    return text

# Apply cleaning
df['cleaned_content'] = df['content'].apply(clean_text)  
#df.apply(clean_text)

# Save cleaned data
df.to_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analytics/data/clean_reviews.csv", index=False)
print("Cleaned reviews saved to data/clean_reviews.csv")






