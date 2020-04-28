import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awsdeployer",
    version="0.0.3",
    author="Guilherme Borges",
    author_email="guilherme@guilhermeborges.net",
    description="Collection of some scripts to automate AWS Lambda deployments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgtpepperpt/awsdeployer",
    packages=['awsdeployer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    scripts=['bin/lambda', 'bin/apigateway']
)