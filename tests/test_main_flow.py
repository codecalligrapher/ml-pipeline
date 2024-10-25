from prefect import flow
from prefect.testing.utilities import prefect_test_harness

from src.flows.main import main_flow


def test_main_flow():
    with prefect_test_harness():
        main_flow()
