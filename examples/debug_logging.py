"""
DEBUG-level logging example.

Shows how DEBUG logs work and how min_level controls logging.
"""

import pandas as pd
from dfflow import DFLogger

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

logger = DFLogger(
    log_file="debug.log",
    min_level="DEBUG"
)

logger.debug("Debug: Raw DataFrame loaded", df)
logger.info("Info: DataFrame ready for processing", df)

print("DEBUG logging completed")
