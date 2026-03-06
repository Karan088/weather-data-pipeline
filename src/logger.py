import logging
import os
from datetime import datetime
from .config import LOG_FOLDER

def setup_logger():

    os.makedirs(LOG_FOLDER, exist_ok=True)

    log_file = f"{LOG_FOLDER}/pipeline_{datetime.now().date()}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging
