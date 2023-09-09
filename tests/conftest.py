import logging
from pathlib import Path
import pytest
import requests

LOGGER = logging.getLogger()
DATASET_URL = "https://github.com/treselle-systems/customer_churn_analysis/blob/master/WA_Fn-UseC_-Telco-Customer-Churn.csv"
DATASET_FILENAME = "Telco-Customer-Churn.csv"


@pytest.fixture(scope="session")
def download_dataset():
    url = DATASET_URL
    r = requests.get(url, allow_redirects=True)
    file_path = Path(__file__).parent / "data" / DATASET_FILENAME
    if not file_path.exists():
        LOGGER.info("Downloading test dataset")
        file_path.parent.mkdir(exist_ok=True)
        file_path.write_bytes(r.content)
    else:
        LOGGER.info("Dataset found, skipping download")
