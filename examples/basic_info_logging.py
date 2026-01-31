"""
Basic INFO-level logging example.

Demonstrates how to log a DataFrame using DFLogger.info().
"""

import pandas as pd
from dfflow import DFLogger

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Maclin", "DiCaprio"],
    "Age": [23, 25]
})

# Initialize logger
logger = DFLogger(
    log_file="basic_info.log",
    min_level="INFO"
)

# Log DataFrame
logger.info("Loaded initial DataFrame", df)

print("Basic INFO logging completed")
