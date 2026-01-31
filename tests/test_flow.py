import pandas as pd
from dfflow.flow import FlowPipeline
from dfflow.logger import DFLogger


def test_pipeline_logging(tmp_path):
    df = pd.DataFrame({"A": [1, None]})

    def drop_na(df):
        return df.dropna()

    log_file = tmp_path / "pipeline.log"
    logger = DFLogger(log_file=str(log_file))

    pipeline = FlowPipeline(logger)
    pipeline.add_step("drop_na", drop_na)

    result = pipeline.run(df)

    assert result.shape == (1, 1)
    assert "drop_na" in log_file.read_text()
