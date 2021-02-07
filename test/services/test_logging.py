import os
from app import setup_logging
import app.core.config as config
from shutil import rmtree


def test_logging():
    logger = setup_logging("testing", log_file="Tester_rescue_labeler.log")
    logger.info("Test Log")

    assert os.path.exists(config.LOG_DIR)
    assert any(
        map(lambda fname: fname.startswith("Tester_"), os.listdir(config.LOG_DIR))
    )
    rmtree(config.LOG_DIR)
    assert not os.path.exists(config.LOG_DIR)
