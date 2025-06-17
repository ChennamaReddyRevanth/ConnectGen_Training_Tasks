#Below function, return the minimum, maximum and average salary of each department in the company
def salary_statistics(df):
    #here groupby function, groups the values according to the department.
    #agg() allows you to apply one or more aggregation functions to specific columns or the entire DataFrame, providing flexibility in summarizing and analyzing data. 
    return df.groupby("department")["salary"].agg(['min', 'max', 'mean'])
