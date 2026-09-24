# Exercise 1

def fibonacci(n):
    prev_no = 0    # previous number
    new_no = 1      # new number 


    if n == 0:
        return 0

    for i in range(n):
        next_no = prev_no + new_no
        prev_no = new_no
        new_no = next_no

    return prev_no

# Exercise 2

def to_binary(n):
    if n == 0:
        return "0"
    else:
        return to_binary(n // 2) + str(n % 2)


# Exercise 3

import pandas as pd
import numpy as np

pd.options.display.max_rows = 100  # default is 60 rows

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
# df_bellevue = pd.read_csv('./data/.../mydata.csv')  # you can also reference locally stored data



# Task 1
def task_1():
    df = df_bellevue.copy()

    # The gender column contains messy/missing values that need to be standardized
    print("Cleaning the gender column before counting missing values.")

    df["gender"] = df["gender"].replace(r"^\s*$", pd.NA, regex=True)

    missing_counts = df.isna().sum()

    return missing_counts.sort_values().index.tolist()


# Task 2
def task_2():
    df = df_bellevue.copy()

    print("Converting the year column to numeric in case it contains messy values.")

    df["year"] = pd.to_numeric(df["year"], errors="coerce")

    result = (
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
    )

    return result


# Task 3
def task_3():
    df = df_bellevue.copy()

    print("Cleaning gender and converting age to numeric before calculating averages.")

    df["gender"] = df["gender"].replace(r"^\s*$", pd.NA, regex=True)
    df["gender"] = df["gender"].astype("string").str.strip()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    return df.groupby("gender")["age"].mean()


# Task 4
def task_4():
    df = df_bellevue.copy()

    print("Removing missing profession values before finding the most common professions.")

    df["profession"] = df["profession"].replace(r"^\s*$", pd.NA, regex=True)

    return df["profession"].dropna().value_counts().head(5).index.tolist()

# Exercise 4


from collections import defaultdict

memo = defaultdict(int)

def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    
    return memo[n]

