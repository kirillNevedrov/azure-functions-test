import json
import logging
import pickle

import azure.functions as func


def pi_digits_Python(digits):
    scale = 10000
    maxarr = int((digits / 4) * 14)
    arrinit = 2000
    carry = 0
    arr = [arrinit] * (maxarr + 1)
    output = ""

    for i in range(maxarr, 1, -14):
        total = 0
        for j in range(i, 0, -1):
            total = (total * j) + (scale * arr[j])
            arr[j] = total % ((j * 2) - 1)
            total = total / ((j * 2) - 1)

        output += "%04d" % (carry + (total / scale))
        carry = total % scale

    return output


def main(msg: func.QueueMessage) -> None:
    msg_body = msg.get_body()
    msg_body = json.loads(msg_body)

    digit_string = pi_digits_Python(7000)

    result = json.dumps({
        'id': msg_body['id'],
        'digit_string_len': len(digit_string)
    })

    logging.info('Python QUEUE trigger processed an event: %s', result)
