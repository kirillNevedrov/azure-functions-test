import json
import uuid

from azure.core.exceptions import ResourceExistsError
from azure.storage.queue import QueueClient, TextBase64EncodePolicy

connection_string = ''

def run():
    queue_client = QueueClient.from_connection_string(
        connection_string,
        'test-fan-in-fan-out-1',
        message_encode_policy=TextBase64EncodePolicy()
    )
    try:
        queue_client.create_queue()
    except ResourceExistsError:
        pass

    queue_client.send_message(json.dumps({
        'chunks_ids': [str(uuid.uuid1()) for i in range(0, 300)]
    }))

    test = 1


if __name__ == "__main__":
    run()
