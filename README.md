# dfflow
![PyPI](https://img.shields.io/pypi/v/dfflow)
![Python](https://img.shields.io/pypi/pyversions/dfflow)
![pandas](https://img.shields.io/badge/pandas-supported-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Lightweight pandas DataFrame logging and flow pipeline tracker.

---

## 📌 What is this?

**dfflow** is a simple, easy-to-use Python package for:
- Logging pandas DataFrame transformations step by step
- Saving logs in text or JSON format
- Building reusable pipeline-style data flows

---

## 📌 Features

✅ Automatic DataFrame transformation logging  
✅ Text and JSON log formats supported  
✅ Easy pipeline-style processing  
✅ Customizable logging  

---

## 📌 Installation

```bash
pip install dfflow
```

---

## 📌 Requirements

- Python >=3.7
- pandas >=1.3

To install requirements:

```bash
pip install -r requirements.txt
```

---

## 📌 Usage Example 1

```python
import pandas as pd
from dfflow import DFLogger, FlowPipeline, drop_nulls
import os
os.makedirs('examples', exist_ok=True)

logger = DFLogger()
pipe = FlowPipeline(logger=logger)

pipe.add_step("Drop Nulls", drop_nulls)

df = pd.DataFrame({
    'name': ['Suresh', None, 'Jerry', 'Sunil', 'Linga'],
    'age': [23, 26, None, 23, 24]
})

pipe.run(df)

```
---
## 📌 Usage Example 2

```python
import pandas as pd
from dfflow import DFLogger, FlowPipeline
from dfflow.cleaning import drop_nulls, lowercase_columns
from dfflow.profile import profile_summary

# Create a sample DataFrame
data = {
    "Name": ["Suresh", None, "Sunil", "Shiva", "Linga"],
    "Age": [23, 26, 23, 24, None]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# Setup the DFLogger
logger = DFLogger(
    log_file='dfflow_log2.txt',  # Log file path
    mode='text'                          # 'text' or 'json'
)

# Create the FlowPipeline
pipe = FlowPipeline(logger=logger)

# Add cleaning steps
pipe.add_step("Drop Nulls", drop_nulls)
pipe.add_step("Lowercase Columns", lowercase_columns)

# Run the pipeline
result_df = pipe.run(df)

print("Final Cleaned DataFrame:")
print(result_df)
print("\n")

# Profile Summary
summary = profile_summary(result_df)
print("Profile Summary:")
print(summary)

```
---

## 📌 Project Structure

```
dfflow/              # Main package folder
│
├── __init__.py
├── logger.py        # Core logging class (DFLogger)
├── decorators.py    # log_step decorator
├── flow.py          # FlowPipeline logic
├── cleaning.py      # Cleaning steps (drop_nulls, lowercase_columns)
├── profile.py       # Profile utilities
├── utils.py         # Helper functions
│
examples/            # Usage demos
│   ├── dfflow_log.txt
│   ├── dfflow_log2.txt
│   ├── flow_demo.py
│   └── flow_demo2.py
│
tests/               # Unit tests
│   ├── __init__.py
│   ├── test_cleaning.py
│   ├── test_flow.py
│   ├── test_logger.py
│   └── test_profile.py
│
LICENSE              # MIT License
README.md            # Project description
requirements.txt     # Dependencies
setup.py             # Packaging configuration

```


---

## 📌 Author

Maintained by **Suresh K**  
📧 Email: sureshstr38@gmail.com  
🌐 GitHub: [suressssz](https://github.com/suressssz)

---

## 📌 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
