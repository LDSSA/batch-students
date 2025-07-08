import pandas as pd
import numpy as np

def get_data(p, ax=0):
    """Gets data from a plot and concatenates it.
    This is necessary for hashing the plot results.
    """
    all_x_data = []
    lines = p.axis.get_lines()
    collections = axis.collections
    if len(lines) > 0:
        all_x_data.append(np.concatenate([x.get_xydata()[:, ax] for x in lines]))
    if len(collections) > 0:
        all_x_data.append(np.concatenate([x.get_offsets()[:, ax] for x in collections]))
    return np.concatenate(all_x_data, axis=0)

def ex_3_dataset(df):
    # Groupby the expertise level and get the mean of the salaries
    grouped = df.groupby('Experience Level')['Salary'].mean().reset_index()
    # Define a custom order of indices
    custom_order = [0, 2, 3, 1]
    # Reindex the DataFrame based on the custom order
    return grouped.reindex(custom_order).reset_index(drop=True)

def ex_6_dataset(df):
    # Median salary for selected job titles
    return df[df['Job Title'].isin(['Data Engineer','Data Scientist','Data Analyst'])
    ].groupby('Job Title')['Salary'].median()
