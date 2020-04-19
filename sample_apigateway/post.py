import json


def lambda_handler(event, context):
    print('POST')
    print(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
