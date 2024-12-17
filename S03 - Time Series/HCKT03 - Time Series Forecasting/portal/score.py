import pandas as pd
import numpy as np


def load(file):
    """Load the data from a file-like object.
    This function will be used to load both the y_true and y_pred objects from
    a file-like object.
    Args:
        file (file object): source of data
    Returns:
        object: Python object
    Examples:
        def load(file):
            return pandas.read_csv(file)
        with open('path/to/file') as file:
            y_true = load(file)
    """
    
    return pd.read_csv(file, header=None)


def validate(y_true, y_pred):
    """Validate that y_pred is a valid prediction
    Args:
        y_true: True values object
        y_pred: Predicted values object
    Returns:
        bool: Validation succeeded, if false a generic error message will be
              supplied
    Raises:
        Any exception will be caught and str(exc) presented to the students
    Example:
        def validate(y_true, y_pred):
            if y_pred.shape != y_true.shape:
                raise ValueError("Expected shape %s" % y_true.shape)
            return True
    """
    if y_pred.shape != y_true.shape:
        raise ValueError(f"Expected shape {y_true.shape}")

    return True


def score(y_true, y_pred):
    """Calculate the mean absolute error (MAE) between true and predicted values.
    This function computes the mean absolute error (MAE). NaN values 
    in either `y_true` or `y_pred` are ignored during the computation.

    Args:
        y_true: True values object (e.g., pandas Series or NumPy array)
        y_pred: Predicted values object (e.g., pandas Series or NumPy array)

    Returns:
        float: The calculated mean absolute error as a floating-point number.

    Example:
        def score(y_true, y_pred):
            return np.nanmean(np.abs(y_true - y_pred))
        y_true = pd.Series([1.0, 2.0, 3.0, np.nan])
        y_pred = pd.Series([1.1, 2.0, 2.9, 4.0])
        result = score(y_true, y_pred)  # Output: 0.06666666666666665
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    my_score = np.nanmean(np.abs(y_true - y_pred))
    
    return float(my_score)