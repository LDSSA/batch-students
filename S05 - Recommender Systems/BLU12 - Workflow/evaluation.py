import sys
import os
import pandas as pd
import numpy as np


def data_reader(y_file: str):
    """
    Import data from solution .csv file,
    """

    y_path = os.path.join('data', y_file)
    df_ = pd.read_csv(y_path, header=None).set_index(0).sort_index()
    return df_


def validate_solution(df_true: pd.DataFrame, df_pred: pd.DataFrame):
    
    if df_true.shape[0] != df_pred.shape[0]:
        raise ValueError(
            f"Wrong number of users, expected {df_true.shape[0]} got {df_pred.shape[0]}"
        )

    users_set_true = set(df_true.index)
    users_set_pred = set(df_pred.index)
    
    if users_set_true != users_set_pred:
        raise ValueError(
            'Unexpected user ids, please check that you are providing '
            'recommendations for the correct users'
        )
    
    if df_pred.shape[1] < df_true.shape[1]:
        raise ValueError(
            f"Not enough recommendations were provided, "
            f"expected at least {df_true.shape[1]} got {df_pred.shape[1]}")


def precision_k(actual: list, predicted: list, k=50):
    if len(actual)<k or len(predicted)<k:
        raise ValueError(f'Not enough recommendations to calculate precision @k for k={k}.')
    return sum([1 for i in predicted if i in actual])/len(predicted)


def average_precision_k(actual, predicted, k=50):
    if len(actual)<k or len(predicted)<k:
        raise ValueError(f'Not enough recommendations to calculate average precision @k for k={k}.')
    mapk=[]
    for i in range(k):
        mapk.append(precision_k(actual,predicted[:i+1],i+1))
    return np.mean(mapk)


def mean_average_precision_k(actual: pd.DataFrame, predicted: pd.DataFrame, k=50):
    avg_precision=[]
    for i in predicted.index:
        avg_precision.append(average_precision_k(actual.loc[i].to_numpy(),predicted.loc[i].to_numpy(),k))
    return np.mean(avg_precision), avg_precision


def evaluate_solution(y_pred_file: str, y_true_file=None):
    """
    Evaluate the solution.
    The number of recommendations used for evaluation (@k) is equal to the number of /
    recommendations in the test data.
    """
    
    if y_true_file is None:
        df_true = data_reader("test_recommendations.csv")
    else:
        df_true = data_reader(f"{y_true_file}.csv")

    df_pred = data_reader(f"{y_pred_file}.csv")
    
    validate_solution(df_true, df_pred)
    
    k=df_true.shape[1]
    return mean_average_precision_k(df_true, df_pred, k)
