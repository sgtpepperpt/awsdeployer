# def success(body={}):
#     return json.dumps({
#         'gatewayResponse': True,
#         'status': 'success',
#         'type': 'success',
#         'body': body
#     })


def error(error_code, user_message=''):
    import json
    return json.dumps({
        'gatewayResponse': True,
        'status': 'error',
        'type': error_code,
        'userMessage': user_message
    })
