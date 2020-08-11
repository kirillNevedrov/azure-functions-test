import json
import uuid

from azure.core.exceptions import ResourceExistsError
from azure.storage.queue import QueueClient, TextBase64EncodePolicy


def run():
    queue_client = QueueClient.from_connection_string(
        'DefaultEndpointsProtocol=https;AccountName=kirillnevedrovtestfuncti;AccountKey=Q4GJP+r+m4uUJ9OFxZ+92r+jZi0l7KaS1gMZgaub+rJDbyCK7OZBupO9SJjX6oA116U2PDEJAyhoAI4+WCavQg==;EndpointSuffix=core.windows.net',
        'macro-scan-train',
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
