import numpy as np
from model.forest import preprocess
import pytest


def test_valid(download_dataset):
    X, y = preprocess(pytest.DATASET_PATH)
    assert len(X) == 10348
    for col in ["customerID", "gender", "PhoneService", "Contract", "TotalCharges"]:
        assert col not in X.columns

    assert X["tenure"].min() >= 0. and X["tenure"].max() <= 1.
    assert X["MonthlyCharges"].min() >= 0. and X["MonthlyCharges"].max() <= 1.

    assert y.dtype == np.dtype("int")
    assert y.min() == 0 and y.max() == 1

    # Check for equal representation of churned and not churned clients
    # value_counts for 0 and 1 should be the same, thus set of these 2 numbers is 1 number
    assert len(set(y.value_counts())) == 1
