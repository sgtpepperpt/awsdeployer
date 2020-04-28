import json


def lambda_handler(event, context):
    print('DELETE')
    print(event)

    return json.dumps({'body': {'msg': 'Hwllo Delete'}})
