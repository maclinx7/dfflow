# dfflow
![PyPI](https://img.shields.io/pypi/v/dfflow)
![Python](https://img.shields.io/pypi/pyversions/dfflow)
![pandas](https://img.shields.io/badge/pandas-supported-blue)
![License](https://img.shields.io/badge/license-MIT-green)

[![PyPI version](https://badge.fury.io/py/dfflow.svg)](https://pypi.org/project/dfflow/)
[![Python Versions](https://img.shields.io/pypi/pyversions/dfflow)](https://pypi.org/project/dfflow/)
[![Tests](https://github.com/maclin-oss/dfflow/actions/workflows/tests.yml/badge.svg)](https://github.com/maclin-oss/dfflow/actions/workflows/tests.yml)
[![License](https://img.shields.io/pypi/l/dfflow)](https://pypi.org/project/dfflow/)


**dfflow** is a **Lightweight Python utility tool** for logging, tracking, and debugging Pandas DataFrame workflows.

It provides:
- Structured DataFrame logging with log levels
- Step-based pipeline execution
- Lightweight DataFrame profiling
- Clean, ML-friendly APIs

---

## Why dfflow?

In real ML projects:

- DataFrames change at every step
- Debugging data issues is painful
- Standard logging libraries do not understand DataFrames

**dfflow solves this gap** by providing:

- Visibility into DataFrame transformations
- Reproducible pipeline execution
- Minimal overhead with maximum clarity

---

## Installation

```bash
pip install dfflow
```
---
## Core Components

- **DFLogger** — DataFrame-aware logger

- **FlowPipeline** — Step-based DataFrame pipeline

- **Decorators** — Lightweight step tracking

- **Cleaning utilities** — Common preprocessing helpers

- **Profiling utilities** — Quick DataFrame inspection

---
## DFLogger
### Class: DFLogger

A DataFrame-aware logger supporting:

- Log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`)
- Text or JSON logging
- Log-level filtering using `min_level`


### Parameters

| Parameter   | Description                       |
| ----------- | --------------------------------- |
| `log_file`  | Output log file path              |
| `mode`      | Logging format (`text` or `json`) |
| `min_level` | Minimum log level to record       |


### Logging Methods

| Method                                 | Description                                  |
|----------------------------------------|----------------------------------------------|
| `debug(message: str, df: DataFrame)`   | Logs detailed debugging information          |
| `info(message: str, df: DataFrame)`    | Logs standard pipeline progress              |
| `warning(message: str, df: DataFrame)` | Logs potential data issues (e.g., row drops) |
| `error(message: str, df: DataFrame)`   | Logs critical failures or invalid states     |


### Usage

```python
import pandas as pd
from dfflow import DFLogger

df = pd.DataFrame({"A": [1, 2], 
                   "B": [3, 4]})

logger = DFLogger(
    log_file="app.log",
    mode="text",
    min_level="INFO"
)

logger.info("Loaded DataFrame", df)

```
---
## FlowPipeline
### Class: FlowPipeline

`FlowPipeline` executes DataFrame transformations sequentially while optionally logging each step.

**Key Features**:

- Explicit step tracking
- Clean integration with `DFLogger`
- Simple, readable pipeline structure


### Methods

| Method                                | Description                                                     |
|---------------------------------------|-----------------------------------------------------------------|
| `add_step(name: str, func: Callable)` | Add a transformation step to the pipeline                       |
| `run(df: DataFrame) -> DataFrame`     | Executes all steps sequentially and returns the final DataFrame |


### Usage

```python
import pandas as pd
from dfflow import DFLogger, FlowPipeline, drop_nulls, lowercase_columns

df = pd.DataFrame({"Name": ["Maclin", None],
                   "Age": ["23", None]})

logger = DFLogger()
pipeline = FlowPipeline(logger)

pipeline.add_step("Drop Nulls", drop_nulls)
pipeline.add_step("Lowercase Columns", lowercase_columns)

result = pipeline.run(df)
print(result)
```
---
## Decorators

`log_step` is a decorator used to mark DataFrame transformation steps.

### Purpose

- Provides simple step-level tracking
- Prints completion messages for better visibility
- Used internally by cleaning utilities but can also be applied to custom functions

### Usage

```python
import pandas as pd
from dfflow import log_step

df = pd.DataFrame({"A": [5, 10],
                  "B": [15, 20]})

@log_step("Normalize Columns")
def normalize(df):
    return df/df.max()

normalized_df = normalize(df)
print(normalized_df)
```
---

## Cleaning Utilities

- `drop_nulls(df)` -> Removes rows containing missing values.
```python
import pandas as pd
from dfflow import drop_nulls

df = drop_nulls(df)
print(df)
```
- `lowercase_columns(df)` -> Converts all column names to lowercase.
```python
import pandas as pd
from dfflow import lowercase_columns

df = lowercase_columns(df)
print(df)
```
---

## Profiling Utilities

Generates a quick summary of a DataFrame.

**Includes**:

- Shape
- Column names
- Null counts
- Data types


### Usage

```python
import pandas as pd
from dfflow import profile_summary

summary = profile_summary(df)
print(summary)
```
---

## Examples

Practical usage examples are available in the
[`examples/`](./examples) directory, including:

- Basic INFO and DEBUG logging
- Pipeline execution with logging levels
- JSON logging
- Lightweight DataFrame profiling

---

## License

This project is licensed under the MIT License.
