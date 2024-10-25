from datetime import timedelta
from pathlib import Path
from typing import Dict, List

import yaml
from pydantic import BaseModel


class FeatureConfig(BaseModel):
    numerical_columns: List[str]
    categorical_columns: List[str]
    date_columns: List[str]
    target_column: str


class ModelConfig(BaseModel):
    type: str
    params: Dict
    features: List[str]
    evaluation_metric: str


class PathConfig(BaseModel):
    data_dir: Path
    raw_dir: Path
    interim_dir: Path
    processed_dir: Path
    feature_dir: Path
    model_dir: Path


class Config(BaseModel):
    paths: PathConfig
    features: FeatureConfig
    model: ModelConfig
    cache_ttl: int
    random_state: int


def load_config(config_path: str = "config.yaml") -> Config:
    with open(config_path) as f:
        config_dict = yaml.safe_load(f)
    return Config(**config_dict)
