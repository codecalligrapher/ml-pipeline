import logging
from typing import Dict, Optional

from prefect import flow

# from ..models.evaluate import evaluate_model
# from ..models.train import train_model
from mlpipeline.utils.config import Config, load_config

from .feature_engineering import feature_engineering_flow

logger = logging.getLogger(__name__)


@flow(name="ml_pipeline")
def main_flow(
    table_paths,
    config_path: str = "config.yaml",
    model_uri: Optional[str] = None,
) -> dict:
    """Main ML pipeline flow"""
    logger.info("Starting main pipeline flow")

    # Load config
    config = load_config(config_path)

    # Feature engineering
    features_path = feature_engineering_flow(table_paths, config)

    return {"f1": 1.00}
