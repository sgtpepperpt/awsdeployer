# AWSDeployer

Collection of some scripts to automate AWS Lambda deployments. They are useful for quick development and deployment of AWS Lambda functions and layers, as well as a REST API Gateway integration. Just set your working directory, your __awsdeploy__ configs and you should be good to focus on actual development.

Currently supporting Python.

---

## Lambda Deployer
Easily deploy Lambda functions and their layers.

### Usage
These scripts assume a working directory like that of sample: 
* `awsdeploy.ini` file with your secrets (see sample file)
* `awsdeploy_lambda.json` with your layer and function configurations
* `function_name.py` files, one for each of your Lambda functions

The main script is `lambda.py`, which accepts the following commands:
* `./lambda.py layer <layer-name>`: deploy layer "layer-name" into AWS
* `./lambda.py new <function-name>`: deploy new function "function-name" into AWS (takes care of default IAM)
* `./lambda.py config [<function-name>]`: update all function configs in AWS (specify a function name to only update that function's configs)
* `./lambda.py code [<function-name>]`: ditto for function code
* `./lambda.py <function-name>`: if no option above is matched, the specified function has its code and configs updated **(probably the most common case)**

Tip: all <function-name> parameters can be replaced by a __shorthand__, which you can specify in your `awsdeploy_configs.json`.

---

## API Gateway Deployer
Easily deploy API gateway, handling input parameters and error codes, so you can focus on the code.

### Usage
These scripts assume a working directory like that of sample: 
* `awsdeploy.ini` file with your secrets (see sample file)
* `awsdeploy_api.json` with your API definition in JSON (NOT nested!)
* `function_xxxx.py` files, one for each of your Lambda functions associated with the endpoints

The `api_gateway.py` script accepts two commands:
* `./api_gateway.py all`: deploy the full API (destroys already existing ones)
* `./api_gateway.py <method> <path>`: deploy a single method (also destroys already existing ones)

The script also helps automating response codes, which you can define in `ApiResponses.py`. They are automatically deployed into API Gateway and caught by it, as long as you use the return functions in `gateway_responses.py`.
