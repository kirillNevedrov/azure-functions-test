from datetime import datetime
from azure.eventgrid import EventGridClient
from msrest.authentication import TopicCredentials
import uuid


def publish_event():
    try:
        for i in range(0, 100):
            credentials = TopicCredentials(
                "8l3ToYeSM1+JgGP8QX+g3i9HHyHt6iqo2K5roH2YO+g="
            )
            event_grid_client = EventGridClient(credentials)

            event_grid_client.publish_events(
                "kirill-nevedrov-test-topic-1.northeurope-1.eventgrid.azure.net",
                events=[{
                    'id': str(uuid.uuid1()),
                    'subject': "Sample subject",
                    'data': {
                        'key': 'Sample Data'
                    },
                    'event_type': 'SampleEventType',
                    'event_time': datetime(2018, 5, 2),
                    'data_version': 1
                }])

        test = 1
    except Exception as ex:
        pass


def run():
    publish_event()


if __name__ == "__main__":
    run()
