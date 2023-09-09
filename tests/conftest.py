import logging
from pathlib import Path
import pytest
import requests


LOGGER = logging.getLogger()


def pytest_configure():
    pytest.DATASET_URL = "https://raw.githubusercontent.com/treselle-systems/customer_churn_analysis/master/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    pytest.DATASET_PATH = Path(__file__).parent / "data" / "Telco-Customer-Churn.csv"


@pytest.fixture(scope="session")
def download_dataset():
    url = pytest.DATASET_URL
    r = requests.get(url, allow_redirects=True)
    if not pytest.DATASET_PATH.exists():
        LOGGER.info("Downloading test dataset")
        pytest.DATASET_PATH.parent.mkdir(exist_ok=True)
        pytest.DATASET_PATH.write_bytes(r.content)
    else:
        LOGGER.info("Dataset found, skipping download")
