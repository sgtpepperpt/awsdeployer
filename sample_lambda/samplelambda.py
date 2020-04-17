import json
import numpy


def lambda_handler(event, context):
    print(numpy.array([[1, 2], [3, 4]]))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
