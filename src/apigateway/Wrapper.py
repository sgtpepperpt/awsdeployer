from src.apigateway.ApiResponses import responses
from src.apigateway.GatewayHandler import GatewayHandler
from src.apigateway.Templater import *
from src.util import build_path


class ApiWrapper:
    """This class provides higher-level primitives for API Gateway actions"""
    def __init__(self, aws_config):
        self.aws = aws_config
        self.gateway_handler = GatewayHandler(self.aws)

    def create_method(self, path, method, configs):
        # get resource id to operate on
        resource_id = self.get_resource_id(path)

        # if method already exists, delete it to be able to replace everything
        if self.gateway_handler.has_method(resource_id, method):
            print('Deleting pre-existing method...')
            self.gateway_handler.delete_method(resource_id, method)

        print('Creating method {0} at resource {1}'.format(method, resource_id))

        # get necessary configs
        lambda_function = configs['function']

        # create request objects based on templates
        request_parameters = create_request_parameters(configs)
        request_body = configs['request_body'] if 'request_body' in configs else []
        request_template = create_request_template(request_parameters, path_parameters=get_path_parameters(path), request_body=request_body)

        # create response objects based on templates
        response_parameters = create_response_parameters(configs)

        # create method and integration with lambda
        self.gateway_handler.create_method(resource_id, method, request_parameters)
        self.gateway_handler.create_integration(resource_id, method, lambda_function, request_template)

        # create responses for sucess, all programmed errors, and catchall
        # (works for any non-empty error string; empty would match 200 too)
        self.gateway_handler.create_method_response(resource_id, method, '200', response_parameters)
        self.gateway_handler.create_integration_response(resource_id, method, '200', response_parameters, '', get_success_response_template())

        for response in responses.keys():
            regex = '^\\{{ "gatewayResponse": true, "status": "error", "type": "{0}", "userMessage": " " }}$'.format(response)
            regex = regex.replace(' ', '(.|\\s)*')

            self.gateway_handler.create_method_response(resource_id, method, str(responses[response]), response_parameters)
            self.gateway_handler.create_integration_response(resource_id, method, str(responses[response]), response_parameters, regex, get_error_response_template())

        # catchall (Bad Gateway, should catch Lambda errors such as timeout or syntax errors)
        self.gateway_handler.create_method_response(resource_id, method, '502', response_parameters)
        self.gateway_handler.create_integration_response(resource_id, method, '502', response_parameters, '\s*.+\s*', get_error_catchall_response_template())

    def create_resource(self, path):
        if self.get_resource_id(path):
            return

        # get tree of resources
        parts = path.split('/')[1:]

        parent_resource_id = self.get_resource_id('/')
        for i in range(len(parts) + 1):
            path_to_check = build_path(parts[:i])
            resource_id = self.get_resource_id(path_to_check)

            if not resource_id:
                parent_resource_id = self.gateway_handler.create_resource(parent_resource_id, parts[i-1])['id']
            else:
                parent_resource_id = resource_id

    def get_resource_id(self, path):
        resources = self.gateway_handler.get_resources()

        for r in resources:
            if r['path'] == path:
                return r['id']

        return None

    def deploy_api(self):
        self.gateway_handler.deploy(self.aws['stage'])
