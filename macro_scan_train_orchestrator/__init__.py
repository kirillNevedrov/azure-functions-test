# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import os
import logging
import pickle
import json
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    try:
        logging.info(
            "macro_scan_train_orchestrator started")

        msg_body = context.get_input()

        parallel_tasks = []
        for chunk_id in msg_body['chunks_ids']:
            parallel_tasks.append(context.call_activity(
                'macro_scan_train_activity',
                {
                    'id': chunk_id
                }
            ))

        outputs = yield context.task_all(parallel_tasks)

        test = yield context.call_activity("macro_scan_train_activity_2", outputs)

        return test

        # logging.info('macro_scan_train_orchestrator succeed')
    except Exception as ex:
        logging.exception(
            "macro_scan_train_orchestrator failed", exc_info=ex)

        raise


main = df.Orchestrator.create(orchestrator_function)
