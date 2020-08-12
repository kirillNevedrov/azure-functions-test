# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import json
import azure.functions as func
import azure.durable_functions as df


async def main(msg: func.QueueMessage, starter: str) -> None:
    msg_body = msg.get_body()
    msg_body = json.loads(msg_body)

    client = df.DurableOrchestrationClient(starter)
    await client.start_new('test_orchestrator', None, msg_body)
