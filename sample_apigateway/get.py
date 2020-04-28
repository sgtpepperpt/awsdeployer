from awsdeployer import gatewayres
import time
import json


def lambda_handler(event, context):
    print('GET')

    # test some codes
    if event['r'] == '200':
        return json.dumps({'body': {'test':1}})
    elif event['r'] == '400':
        raise Exception(gatewayres.error('BadRequest', 'Wubbalubbadubdub'))
    elif event['r'] == '500':
        raise Exception(gatewayres.error('InternalServerError', 'JeezMorty'))
    else:
        time.sleep(10)
