# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


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


def main(msg):
    try:
        digit_string = pi_digits_Python(7000)

        return {
            'id': msg['id'],
            'digit_string_len': len(digit_string)
        }
    except Exception as ex:
        logging.exception(
            "test_fan_out_activity failed", exc_info=ex)

        raise
