import pandas

def ex_3_dataset(df):
    # Groupby the expertise level and get the mean of the salaries
    grouped = df.groupby('Expertise Level')['Salary'].mean().reset_index()
    # Define a custom order of indices
    custom_order = [3, 2, 1, 0]
    # Reindex the DataFrame based on the custom order
    return grouped.reindex(custom_order).reset_index(drop=True)

def ex_4_dataset(df):
    title_counts = df['Job Title'].value_counts()
    return df[df['Job Title'].isin(title_counts[title_counts>10].index)]


def ex_6_dataset(df):
    # Groupby the company size and get the median of the salaries
    grouped = df.groupby('Company Size')['Salary'].median().reset_index()
    # Define a custom order of indices
    custom_order = [2, 1, 0]
    # Reindex the DataFrame based on the custom order
    return grouped.reindex(custom_order).reset_index(drop=True)
