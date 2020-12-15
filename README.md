# AWSDeployer

Collection of some scripts to automate AWS Lambda deployments. They are useful for quick development and deployment of AWS Lambda functions and layers, as well as a REST API Gateway integration.

Just set your working directory, your __awsdeployer__ configs and you should be good to focus on actual development.

Currently only supporting Python lambda functions.

---

## Lambda Deployer
Easily deploy Lambda functions and their layers.

### Usage
These scripts assume a working directory like that of sample_lambda:
* `awsdeployer.ini` file with your secrets (see sample file)
* `awsdeployer_lambda.json` with your layer and function configurations
* `function_name.py` files, one for each of your Lambda functions

The executable is `lambda`, which accepts the following commands:
* `$ lambda layer <layer-name>`: deploy layer "layer-name" into AWS (requires docker to build)
* `$ lambda config [<function-name>]`: update all function configs in AWS (specify a function name to only update that function's configs); non-existing functions are created (default Lambda IAM permissions)
* `$ lambda <function-name>`: if no option above is matched, the specified function has its code and configs updated **(probably the most common case)**; non-existing functions are created (default Lambda IAM permissions)

Tip: all <function-name> parameters can be replaced by a __shorthand__, which you can specify in your `awsdeployer_lambda.json`.

### Configs
* `main_file`: specify the main function file (if not present, function_name.py is assumed)
* `additional_files`: additional files to include with the main function file in the deployment

### Special layer building
If you need to build a specific package for your layer (eg. psycopg2) you can use pre and post build hooks for the layer build, and add docker arguments to the command.

To build psycopg2 compile it separately, then use these configs:
```
"layer_configs": {
    "psycopg2layer": {
        "requirements_file": "requirements.txt",
        "requirements_ignore": ["psycopg2"],
        "build_args": "-v ~/psycopg2-build:/bar",
        "pre_build_command": "echo 'Something before pip'",
        "post_build_command": "cp -r /bar /foo/python/psycopg2",
        "common": true
    }
}
```

---

## API Gateway Deployer
Easily deploy API gateway, handling input parameters and error codes, so you can focus on the code.

### Usage
These scripts assume a working directory like that of sample_apigateway:
* `awsdeployer.ini` file with your secrets (see sample file)
* `awsdeployer_api.json` with your API definition in JSON (NOT nested!)
* `function_xxxx.py` files, one for each of your Lambda functions associated with the endpoints

The `apigateway` executable accepts two commands:
* `$ apigateway all`: deploy the full API (destroys already existing ones)
* `$ apigateway <method> <path>`: deploy a single method (also destroys already existing ones)

The script also helps automating HTTP error codes, which you can find in `status_codes.md`. They are automatically
deployed into API Gateway and caught by it, as long as you import the `awsdeployer` package, as seen in `sample_apigateway/get.py`.
If you're not using Python, your errors should follow the following JSON syntax to be caught effectively:
```
{
    'gatewayResponse': True,
    'status': 'error',
    'type': _status_code_from_md_file,
    'userMessage': your_user_message_which_can_be_empty
}
```
