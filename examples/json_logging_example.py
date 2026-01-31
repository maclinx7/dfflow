"""
JSON logging example.

Demonstrates logging DataFrame metadata in JSON format.
"""

import pandas as pd
from dfflow import DFLogger

df = pd.DataFrame({
    "City": ["Chennai", "Bangalore"],
    "Temperature": [35, 28]
})

logger = DFLogger(
    log_file="log.json",
    mode="json",
    min_level="INFO"
)

logger.info("Weather DataFrame logged in JSON format", df)

print("JSON logging completed")
