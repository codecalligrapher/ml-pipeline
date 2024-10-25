import logging
from pathlib import Path
from typing import Dict

from prefect import flow
from prefect.utilities.annotations import quote

# from ..features.user_features import compute_user_features
# from ..features.temporal_features import compute_temporal_features
from mlpipeline.data.io import load_table
from mlpipeline.utils.config import Config

logger = logging.getLogger(__name__)


@flow(name="feature_engineering")
def feature_engineering_flow(table_paths: Dict[str, str], config: Config):
    """Orchestrate feature engineering pipeline"""
    logger.info("Starting feature engineering flow")

    # Load and validate tables
    validated_paths = {}
    for table_name, path in table_paths.items():
        validated_paths[table_name] = load_table(path, config)

    return validated_paths[0]  # HACK
