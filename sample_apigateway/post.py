import json


def lambda_handler(event, context):
    print('POST')
    print(event)

    return json.dumps({'body': {'msg': 'Hwllo Post'}})
