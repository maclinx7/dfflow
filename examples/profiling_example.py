"""
Data profiling example.

Shows how to generate a quick profile summary of a DataFrame.
"""

import pandas as pd
from dfflow import profile_summary

df = pd.DataFrame({
    "Salary": [50000, None, 70000],
    "Bonus": [5000, 7000, None]
})

summary = profile_summary(df)

print("Profile Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")
