# ------------------------What are pandas?----------------------------


# Pandas is a Python library used for working with data sets.

# It has functions for analyzing, cleaning, exploring, and manipulating data


#------------------------Why do we use Pandas?------------------


# Pandas allows us to analyze big data and make conclusions based on statistical theories.

# Pandas can clean messy data sets, and make them readable and relevant.

# Relevant data is very important in data science.

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("student_data.csv")

# print(" Full Data:\n", df)

# Filter students with marks > 80

print(df[df["marks"] > 80])

# print(df["name"])


df.loc[df["name"]=="kalki", "marks"] = 85
print(df[df["name"]=="kalki"])

#TO update any data :

df.loc[df['name']=="kalki" , "marks"] = 85# used to locate through rows and columns

