#! /usr/local/bin/python3
import configparser
import json
import sys

from src.apigateway.Wrapper import ApiWrapper


class AWSApiGatewayDeployer:
    def __init__(self, aws_config, api_configs):
        self.api_wrapper = ApiWrapper(aws_config)
        self.api_configs = api_configs

    def create_method(self, path, method):
        method_configs = self.api_configs[path][method]
        self.api_wrapper.create_method(path, method, method_configs)

        # deploy changes
        self.api_wrapper.deploy_api()

    def create_full_api(self):
        for resource in api_configs.keys():
            self.api_wrapper.create_resource(resource)
            for method in self.api_configs[resource].keys():
                self.create_method(resource, method)

        # deploy changes
        self.api_wrapper.deploy_api()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No argument provided')
        exit(1)

    aws_config_file = 'awsdeploy.ini'
    api_config_file = 'awsdeploy_api.json'

    config = configparser.ConfigParser()
    config.read(aws_config_file)

    aws_config = {
        'region': config['ACCOUNT']['region'],
        'access_key': config['ACCOUNT']['access_key'],
        'secret_key': config['ACCOUNT']['secret_key'],
        'account_id': config['ACCOUNT']['account_id'],

        'api_id': config['API_GATEWAY']['api_id'],
        'stage': config['API_GATEWAY']['stage']
    }

    with open(api_config_file) as json_file:
        api_configs = json.load(json_file)

    api_gateway = AWSApiGatewayDeployer(aws_config, api_configs)

    # interpret terminal input
    arg = sys.argv[1]
    if arg == 'all':
        api_gateway.create_full_api()
    else:
        if len(sys.argv) < 3:
            print('No argument provided')
            exit(1)

        method = sys.argv[1]
        path = sys.argv[2]
        api_gateway.create_method(path, method)
