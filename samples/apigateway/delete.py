import json


def lambda_handler(event, context):
    print('DELETE')
    print(event)

    # you can return a simple json object
    return json.dumps({'body': {'msg': 'Hello Delete'}})
