import pandas as pd
from sklearn.metrics import roc_auc_score


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
    return pd.read_csv(file, index_col='id').sort_index()


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
        raise ValueError("Expected shape %s" % y_true.shape)

    return True


def score(y_true, y_pred):
    """Score the prediction

    Args:
        y_true: True values object
        y_pred: Predicted values object

    Returns:
        float: Score value of the prediction

    Example:
        def score(y_true, y_pred):
            return roc_auc_score(y_true, y_pred)
    """
    return roc_auc_score(y_true, y_pred)

