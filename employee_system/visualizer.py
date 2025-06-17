import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#This function is used to show the performance chart of an each employee.
def plot_avg_scores(df):
    if df.empty or "avg_score" not in df.columns:
        print("No data or 'avg_score' column missing.")
        return

    plt.figure(figsize=(10, 6))
    sns.barplot(x='name', y='avg_score', hue='department', data=df)
    plt.title("Employee Performance (Avg Score)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# This function is used to Show Rating Distribution
def plot_rating_distribution(df):
    if df.empty or "rating" not in df.columns:
        print("No data or 'rating' column missing.")
        return

    plt.figure(figsize=(6, 5))
    sns.countplot(x='rating', data=df, palette='Set2')
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.show()
