# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(msg):
    try:
        total_count = len(msg)

        logging.info(f"test_fan_in_activity total_count: {total_count}")

        return total_count
    except Exception as ex:
        logging.exception(
            "test_fan_in_activity failed", exc_info=ex)

        raise
