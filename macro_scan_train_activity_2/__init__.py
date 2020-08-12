# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import os
import logging
import json
# import time
from typing import Any
from azure.core.exceptions import ResourceExistsError


def main(msg):
    try:
        logging.info(
            "macro_scan_train_orchestrator succeed")

        return 'test'

    except Exception as ex:
        logging.exception(
            "macro_scan_train_activity_2 failed", exc_info=ex)

        raise
