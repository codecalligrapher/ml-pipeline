import logging
from datetime import timedelta
from pathlib import Path

import pandas as pd
from prefect import task
from prefect.tasks import task_input_hash

from ..utils.config import Config

logger = logging.getLogger(__name__)


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def load_table(file_path: str, config: Config) -> Path:
    """Load and validate a data table"""
    logger.info(f"Loading data from {file_path}")
    print(file_path)

    df = (
        pd.read_parquet(file_path)
        if file_path.endswith(".parquet")
        else pd.read_csv(file_path)
    )

    if df.empty:
        raise ValueError(f"Empty dataframe loaded from {file_path}")

    # Save validated data
    output_path = config.paths.interim_dir / f"validated_{Path(file_path).stem}.parquet"
    df.to_parquet(output_path)

    return output_path
