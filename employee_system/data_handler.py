#Below function exports the all data to CSV
def export_to_csv(df, filename="employees.csv"):
    df.to_csv(filename, index=False)
