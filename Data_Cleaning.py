# titanic_cleaning.py

import pandas as pd

# Load Titanic dataset
df = pd.read_csv("titanic.csv")  # Make sure titanic.csv is in the same folder

print("Original Shape:", df.shape)

# 1. Drop irrelevant columns
df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)

# 2. Handle missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# 3. Convert categorical columns to numeric
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# 4. Remove any remaining missing data (if any)
df.dropna(inplace=True)

# 5. Save cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("Cleaned Shape:", df.shape)
print("Data cleaning complete. Cleaned file saved as 'titanic_cleaned.csv'")
