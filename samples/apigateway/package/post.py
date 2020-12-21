from awsdeployer import gatewayres
from awsdeployer.exceptions import AmazonException
from awsdeployer.status import Common


def lambda_handler(event, context):
    print('POST')
    print(event)

    if event.get('test') == 'private_error':
        raise ValueError('Private error')
    elif event.get('test') == 'created':
        raise AmazonException(Common.Created)
    else:
        return gatewayres.success({'msg': 'Hello Post'})
