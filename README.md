# AWSDeployer

Collection of some scripts to automate AWS Lambda deployments. They are useful for quick development and deployment of AWS Lambda functions and layers, as well as a REST API Gateway integration. Just set your working directory, your __awsdeploy__ configs and you should be good to focus on actual development.

Currently supporting Python lambda functions.

---

## Lambda Deployer
Easily deploy Lambda functions and their layers.

### Usage
These scripts assume a working directory like that of sample: 
* `awsdeploy.ini` file with your secrets (see sample file)
* `awsdeploy_lambda.json` with your layer and function configurations
* `function_name.py` files, one for each of your Lambda functions

The executable is `lambda`, which accepts the following commands:
* `$ lambda layer <layer-name>`: deploy layer "layer-name" into AWS
* `$ lambda new <function-name>`: deploy new function "function-name" into AWS (takes care of default IAM)
* `$ lambda config [<function-name>]`: update all function configs in AWS (specify a function name to only update that function's configs)
* `$ lambda code [<function-name>]`: ditto for function code
* `$ lambda <function-name>`: if no option above is matched, the specified function has its code and configs updated **(probably the most common case)**

Tip: all <function-name> parameters can be replaced by a __shorthand__, which you can specify in your `awsdeploy_configs.json`.

---

## API Gateway Deployer
Easily deploy API gateway, handling input parameters and error codes, so you can focus on the code.

### Usage
These scripts assume a working directory like that of sample: 
* `awsdeploy.ini` file with your secrets (see sample file)
* `awsdeploy_api.json` with your API definition in JSON (NOT nested!)
* `function_xxxx.py` files, one for each of your Lambda functions associated with the endpoints

The `apigateway` executable accepts two commands:
* `$ apigateway all`: deploy the full API (destroys already existing ones)
* `$ apigateway <method> <path>`: deploy a single method (also destroys already existing ones)

The script also helps automating HTTP error codes, which you can find in `status_codes.md`. They are automatically deployed into API Gateway and caught by it, as long as you import the `awsdeployer` package, as seen in `sample_apigateway/get.py`.
