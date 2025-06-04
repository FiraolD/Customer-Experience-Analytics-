import pandas as pd

# Load raw reviews
df = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/Customer-Experience-Analyticsdata/data/raw_reviews.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.dropna(subset=["content", "score"], inplace=True)

# Normalize dates
df['date'] = pd.to_datetime(df['at']).dt.date

# Save cleaned data
df.to_csv("data/clean_reviews.csv", index=False)
print("Cleaned reviews saved to data/clean_reviews.csv")