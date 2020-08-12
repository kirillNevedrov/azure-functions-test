import json
import uuid

from azure.core.exceptions import ResourceExistsError
from azure.storage.queue import QueueClient, TextBase64EncodePolicy

connection_strings = []


def run():
    for s in connection_strings[1:]:
        queue_client = QueueClient.from_connection_string(
            s,
            'macro-scan-cv',
            message_encode_policy=TextBase64EncodePolicy()
        )
        try:
            queue_client.create_queue()
        except ResourceExistsError:
            pass

        for i in range(0, 33):
            queue_client.send_message(json.dumps({
                'id': str(uuid.uuid1())
            }))

        test = 1


if __name__ == "__main__":
    run()
