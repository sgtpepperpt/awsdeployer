import json


# def gateway_success(body={}):
#     return json.dumps({
#         'gatewayResponse': True,
#         'status': 'success',
#         'type': 'success',
#         'body': body
#     })


def gateway_error(error_code, user_message=''):
    return json.dumps({
        'gatewayResponse': True,
        'status': 'error',
        'type': error_code,
        'userMessage': user_message
    })
