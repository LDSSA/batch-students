import json
import numpy as np

MAPK = 5


def load(file):
    """Load the data from a file-like object.

    This function will be used to load both the y_true and y_pred objects from
    a file-like object.

    Args:
        file (file object): source of data

    Returns:
        object: Python object
    """
    return json.load(file)


def validate(y_true, y_pred):
    """Validate that y_pred is a valid prediction.

    Args:
        y_true: True values object (ground truth dict)
        y_pred: Predicted values object (submission dict)

    Returns:
        bool: Validation succeeded

    Raises:
        ValueError: with message presented to students
    """
    if len(y_pred) != len(y_true):
        raise ValueError(
            "Wrong number of users in the prediction file. "
            f"Expected {len(y_true)} users, got {len(y_pred)} users."
        )

    users_set_true = set(y_true.keys())
    users_set_pred = set(y_pred.keys())

    if users_set_true != users_set_pred:
        missing = users_set_true - users_set_pred
        extra = users_set_pred - users_set_true
        msg = "Unexpected user IDs in submission."
        if missing:
            msg += f" Missing {len(missing)} users."
        if extra:
            msg += f" Found {len(extra)} extra users."
        raise ValueError(msg)

    for user, preds in y_pred.items():
        if not isinstance(preds, list):
            raise ValueError(
                f"Expected a list of recommendations for user {user}, "
                f"got {type(preds).__name__}."
            )

        if len(preds) > MAPK:
            raise ValueError(
                f"Maximum of {MAPK} recommendations per user allowed. "
                f"Got {len(preds)} recommendations for user {user}."
            )

        if len(set(preds)) != len(preds):
            raise ValueError(
                f"Duplicate game IDs found in recommendations for user {user}."
            )

    return True


def average_precision_at_k(actual, predicted, k=MAPK):
    """Compute AP@k for a single user."""
    if not actual:
        return 0.0
    actual_set = set(actual)
    predicted = predicted[:k]
    hits = 0
    score = 0.0
    for i, item in enumerate(predicted):
        if item in actual_set:
            hits += 1
            score += hits / (i + 1)
    return score / min(len(actual_set), k)


def mean_average_precision_at_k(actual, predicted, k=MAPK):
    """Compute mAP@k across all users."""
    ap_scores = []
    for user in actual.keys():
        ap = average_precision_at_k(actual[user], predicted.get(user, []), k)
        ap_scores.append(ap)
    return np.mean(ap_scores)


def score(y_true, y_pred):
    """Score a submission against ground truth.

    Args:
        y_true: dict mapping user_id -> list of relevant game IDs
        y_pred: dict mapping user_id -> list of recommended game IDs

    Returns:
        float: mAP@10 * 1000
    """
    return mean_average_precision_at_k(y_true, y_pred, k=MAPK) * 1000
