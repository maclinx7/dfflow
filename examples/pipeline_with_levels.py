"""
Pipeline example with logging levels.

Demonstrates FlowPipeline + cleaning steps + DFLogger.
"""

import pandas as pd
from dfflow import (
    DFLogger,
    FlowPipeline,
    drop_nulls,
    lowercase_columns,
)

# Sample DataFrame with issues
df = pd.DataFrame({
    "Name": ["Maclin", None, "DiCaprio"],
    "AGE": [23, 25, None]
})

logger = DFLogger(
    log_file="pipeline.log",
    mode="text",
    min_level="INFO"
)

pipeline = FlowPipeline(logger=logger)
pipeline.add_step("Drop Nulls", drop_nulls)
pipeline.add_step("Lowercase Columns", lowercase_columns)

final_df = pipeline.run(df)

print("Pipeline completed successfully")
print(final_df)
