import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#check data types
print("Data Types:")
print(df.dtypes)
print()

# Nominal and Ordinal Categorical Features
# Nominal Categorical Variables
nominal_cat = ["Name","Ticket","Cabin"]

# Ordinal Categorical Variables
ordinal_cat = ["Embarked","Gender"]

# Frequency gender
print("Frequency of gender value:")
print(df["Gender"].value_counts())
print()

# Median value of feature Gender
gender_categories = ["Female","Male"]

df["Gender"] = pd.Categorical(df["Gender"], gender_categories, ordered=True)

median_index = np.median(df["Gender"].cat.codes)
median_gender = gender_categories[int(median_index)]
print(f"Median gender is = {median_gender}")

# count Embarked
print("Count Embarked value:")
print(df["Embarked"].value_counts())
print()

# Median value of feature Embarked
embarked_categories = ["S","C","Q"]

df["Embarked"] = pd.Categorical(df["Embarked"], embarked_categories, ordered=True)

median_index = np.median(df["Embarked"].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(f"Median Embarked is = {median_embarked}")