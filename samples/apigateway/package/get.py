from awsdeployer import gatewayres
from awsdeployer.exceptions import AmazonException
import time


def lambda_handler(event, context):
    print('GET')

    # test some codes
    if event['r'] == '200':
        return gatewayres.success({'test': 1})
    elif event['r'] == '400':
        raise AmazonException('BadRequest', 'Wubbalubbadubdub')
    elif event['r'] == '500':
        raise AmazonException('InternalServerError', 'JeezMorty')
    else:
        time.sleep(10)
