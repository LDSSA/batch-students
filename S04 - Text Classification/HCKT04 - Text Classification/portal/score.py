import pandas as pd
from sklearn.metrics import f1_score


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
            return pandas.read_csv(file, dtypes={"is_helpful": str})
        with open('path/to/file') as file:
            y_true = load(file)
    """
    return pd.read_csv(file, dtype={"class": str})


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
        raise ValueError(f"Expected shape {y_true.shape}, prediction shape {y_pred.shape}")

    return True

def score(y_true, y_pred):
    return f1_score(y_true, y_pred, average="weighted")
