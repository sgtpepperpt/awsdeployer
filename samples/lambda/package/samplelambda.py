import json
import numpy
# import psycopg2

from inner import printer


def lambda_handler(event, context):
    printer.myprinter()

    print(numpy.array([[1, 2], [3, 4]]))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
