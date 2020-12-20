import json
import os

import numpy
# import psycopg2

from inner import printer


def lambda_handler(event, context):
    # test submodules
    printer.myprinter()

    # test env and env packs
    print('env DB_NAME: {0}'.format(os.environ['DB_NAME']))
    print('env EXAMPLE_VARIABLE: {0}'.format(os.environ['EXAMPLE_VARIABLE']))

    # test dependencies
    print(numpy.array([[1, 2], [3, 4]]))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
