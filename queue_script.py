import json
import uuid

from azure.core.exceptions import ResourceExistsError
from azure.storage.queue import QueueClient, TextBase64EncodePolicy

connection_strings = [
    'DefaultEndpointsProtocol=https;AccountName=kirillnevedrovtestfuncti;AccountKey=Q4GJP+r+m4uUJ9OFxZ+92r+jZi0l7KaS1gMZgaub+rJDbyCK7OZBupO9SJjX6oA116U2PDEJAyhoAI4+WCavQg==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc1;AccountKey=bSS7mGxGnynCNTDtomYPZWxBi211RSNKyapKGnXbxTmGDyy4wTkdudUTVf3fVMLd3Bu2Y1W2nYJHBKFJw5CpVw==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc2;AccountKey=8zHqPf+uNKGDvhFGfG4sEg/JY/9sUVEsULBeZRREP9p1XcYIb0y241eFM1nehIEXc6WU17p8vei7DJ5TAVKzLQ==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc3;AccountKey=P/pvuA2J/cFepPhcFZL6uuRCnkSQ6rEOXrFiQaIGOiw1IPbrxwsK190Sr6RoUg5FELlCQMgOyjXDQZd1iRs6NQ==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc4;AccountKey=1eKmtXstO1rj+Bxjq4wFy/vmjVYa0ycmReu5CzDpWJxiackE/jvlbGoIjwqfRWomsIbPtuVZk59fANBDumICOQ==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc5;AccountKey=mNVPbMKGD7qLp4OuYJ/NhuWsZvVMEqAW1m7+T1si9adqM6UoztWW/u992nqmXB1U9Esfeu+f+JXSV4e8iddQhw==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc6;AccountKey=F1pjILvVRCXgYcZ4yWgQDc32GbdIYmX7KGoZoZ5DWYFgCeZwRvbiw94tbt0RnpFE4wfiRoWJUW66HucKNWH2sg==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc7;AccountKey=j1OI9G1i4BDw9B3pKSCg1sR1hqROcfBwpnrpsJ01QlCBUXSN6QHb98FD1H4VzGxHNgMMKZpNpo86HH7mcUxWPg==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc8;AccountKey=0iDLrv/I9Gqv++jqcKUgJVF9J1sElsVFQ9CVZbyygWuGtkefCfZUcSbrBoDNveaBb/qXDgYgP9JIpBb4fueU2g==;EndpointSuffix=core.windows.net',
    'DefaultEndpointsProtocol=https;AccountName=kntestfunc9;AccountKey=BBaKShfMkJ/JuqcD2m0CudEt2rk8gBPLb24aISVctdEA9CR+gZgXJZv4tCMG/uTvt9lAR8nIYOyxRwJsii4ezQ==;EndpointSuffix=core.windows.net'
]


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
