#! /usr/local/bin/python3
import configparser
import sys
import json

from src.FunctionHandler import FunctionHandler
from src.LayerHandler import LayerHandler


class AwsLambdaDeployer:
    def __init__(self, aws_config, layer_configs, function_configs):
        # create handlers for all layers, and store common layer names in an aux list
        self.layer_handlers = {}
        common_layer_names = []
        for layer_name in layer_configs.keys():
            self.layer_handlers[layer_name] = LayerHandler(aws_config, layer_name, layer_configs[layer_name]['requirements_file'])
            common_layer_names.append(layer_name)

        # create function handlers
        self.function_handlers = {}
        for function_name in function_configs.keys():
            layer_names = common_layer_names
            if 'additional_layers' in function_configs[function_name]:
                layer_names += function_configs[function_name]['additional_layers']

            layer_handlers = [self.layer_handlers[i] for i in layer_names]  # get actual layer handlers

            self.function_handlers[function_name] = FunctionHandler(aws_config, function_name, function_configs[function_name], layer_handlers)

    def create_function(self, function_name):
        print('Creating function {}'.format(function_name))
        self.function_handlers[function_name].create()

    def update_all_function_configs(self):
        print('Updating all function configurations')
        for function_name in self.function_handlers.keys():
            self.function_handlers[function_name].update_configs()

    def update_single_function_configs(self, function_name):
        print('Updating {} function configurations'.format(function_name))
        self.function_handlers[function_name].update_configs()

    def update_all_functions_code(self):
        print('Updating all functions code')
        for function_name in self.function_handlers.keys():
            self.function_handlers[function_name].update_configs()
            self.function_handlers[function_name].update_code()

    def update_single_function_code(self, function_name):
        print('Updating {} function code'.format(function_name))
        self.function_handlers[function_name].update_configs()
        self.function_handlers[function_name].update_code()

    def update_layer(self, layer_name, cleanup_old=True, update_functions=True):
        print('Updating {} layer code'.format(layer_name))
        self.layer_handlers[layer_name].compile_new_version()

        if update_functions:
            self.update_all_function_configs()

        if cleanup_old:
            self.layer_handlers[layer_name].cleanup_old_versions()


def expand_shortand(function_configs, shortand):
    if shortand in function_configs.keys():
        return shortand

    for function_name in function_configs.keys():
        if 'shorthand' in function_configs[function_name] and function_configs[function_name]['shorthand'] == shortand:
            return function_name

    print('No function with name or shortand "{0}" found'.format(shortand))
    exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No argument provided')
        exit(1)

    config = configparser.ConfigParser()
    config.read('awsdeploy.ini')

    aws_config = {
        'region': config['ACCOUNT']['region'],
        'access_key': config['ACCOUNT']['access_key'],
        'secret_key': config['ACCOUNT']['secret_key'],
        'account_id': config['ACCOUNT']['account_id'],

        'lambda_prefix': config['PROJECT']['lambda_prefix'],
        'runtime': config['PROJECT']['runtime']
    }

    with open('awsdeploy_configs.json') as json_file:
        data = json.load(json_file)

    layer_configs = data['layer_configs']
    function_configs = data['function_configs']
    lambdas = AwsLambdaDeployer(aws_config, layer_configs, function_configs)

    # interpret terminal input
    arg = sys.argv[1]
    if arg == 'layer':
        if len(sys.argv) < 3:
            print('No argument provided')
            exit(1)

        layer_name = sys.argv[2]
        cleanup_old = True
        update_functions = True
        # if len(sys.argv) >= 4 and sys.argv[3] == '-k' or sys.argv[4] == '-k':
        #     cleanup_old = False
        #
        # if len(sys.argv) >= 4 and sys.argv[3] == '-o' or sys.argv[4] == '-o':
        #     update_functions = False

        lambdas.update_layer(layer_name, cleanup_old=cleanup_old, update_functions=update_functions)

    elif arg == 'new':
        if len(sys.argv) < 3:
            print('No argument provided')
            exit(1)

        function_name = expand_shortand(function_configs, sys.argv[2])
        lambdas.create_function(function_name)

    elif arg == 'config':
        if len(sys.argv) < 3:
            lambdas.update_all_function_configs()
        else:
            function_name = expand_shortand(function_configs, sys.argv[2])
            lambdas.update_single_function_configs(function_name)

    elif arg == 'code':
        if len(sys.argv) < 3:
            lambdas.update_all_functions_code()
        else:
            function_name = expand_shortand(function_configs, sys.argv[2])
            lambdas.update_single_function_code(function_name)

    else:
        # if not a special command then assume update_single_function_code, the most common case
        lambdas.update_single_function_code(expand_shortand(function_configs, arg))
