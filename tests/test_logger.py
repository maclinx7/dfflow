import json
import pandas as pd
import pytest
from dfflow.logger import DFLogger


@pytest.fixture
def df():
    return pd.DataFrame({"A": [1, 2], "B": [3, 4]})


def test_info_logging(tmp_path, df):
    log_file = tmp_path / "info.log"
    logger = DFLogger(log_file=str(log_file))

    logger.info("Info message", df)

    content = log_file.read_text()
    assert "INFO" in content
    assert "Info message" in content


def test_debug_filtered(tmp_path, df):
    """
    DEBUG logs should NOT be written when min_level is INFO.
    File should not be created.
    """
    log_file = tmp_path / "debug.log"
    logger = DFLogger(log_file=str(log_file), min_level="INFO")

    logger.debug("Debug message", df)

    assert not log_file.exists()


def test_debug_allowed(tmp_path, df):
    log_file = tmp_path / "debug_allowed.log"
    logger = DFLogger(log_file=str(log_file), min_level="DEBUG")

    logger.debug("Debug message", df)

    content = log_file.read_text()
    assert "DEBUG" in content
    assert "Debug message" in content


def test_json_logging(tmp_path, df):
    log_file = tmp_path / "log.json"
    logger = DFLogger(log_file=str(log_file), mode="json")

    logger.info("JSON log", df)

    payload = json.loads(log_file.read_text())
    assert payload["level"] == "INFO"
    assert payload["shape"] == [2, 2]


def test_invalid_dataframe():
    logger = DFLogger()

    with pytest.raises(TypeError):
        logger.info("Invalid input", [1, 2, 3])
