import pandas as pd
from dfflow.cleaning import drop_nulls, lowercase_columns


def test_drop_nulls():
    df = pd.DataFrame({"A": [1, None]})
    result = drop_nulls(df)
    assert result.isnull().sum().sum() == 0


def test_lowercase_columns():
    df = pd.DataFrame({"Name": [1], "AGE": [2]})
    result = lowercase_columns(df)
    assert list(result.columns) == ["name", "age"]
