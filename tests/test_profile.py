import pandas as pd
from dfflow.profile import profile_summary


def test_profile_summary():
    df = pd.DataFrame({"A": [1, None]})
    summary = profile_summary(df)

    assert summary["shape"] == (2, 1)
    assert summary["null_counts"]["A"] == 1
