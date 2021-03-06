## UV Provenance API

Current directory contains:
* uv-prov implementation in `src/uvprov_api` folder

VERSION: 0.2

### UV Provenance API Docker container

Using the WF API Docker container:
* `docker pull attxproject/uv-prov` in the current folder;
* running the container `docker run -d -p 4301:4301 attxproject/uv-prov` runs the container in detached mode on the `4301` port (production version should have this port hidden);
* using the endpoints `http://localhost:4301/$versionNb/activity` or `http://localhost:4301/$versionNb/workflow`.

The version number is specified in `src/uvprov_api/app.py` under `version` variable.
In order to run this in a docker container with the UnifiedViews ETL tool.

# UV Provenance API server

## Overview
The WF exposes information from the ETL component (initial use case is the UnifiedViews
and the specific ATTX metadata plugin) in order to exposes Workflow and Activity related information
characteristic to the ETL process. Such information can be consumed in order to be integrated in a graph database.

The WF API requires python 2.7 installed.

## API Endpoints

The workflow REST API has two endpoints along with a health check endpoint:
* `workflow` - retrieve all the workflows and associated steps from the ETL Artifact;
* `activity` - retrieve all successfully completed activites and associated datasets from the ETL Artifact;
* `health` - checks if the application is running.

## Develop
### Build with Gradle

Install [gradle](https://gradle.org/install). The tasks available are listed below:

* do clean build: `gradle clean build`
* see tasks: `gradle tasks --all` and depenencies `gradle depenencies`
* see test coverage `gradle pytest coverage` it will generate a html report in `htmlcov`

### Run without Gradle

To run the server, please execute the following (preferably in a virtual environment):
```
pip install -r pinned.txt
python src/uvprov_api/uvprovapi.py
```

For testing purposes the application requires a running UnifiedViews, one can make a request to the address below to view pipelines and associated steps:

```
http://localhost:4301/$versionNb/workflow
```


The Swagger definition lives here: `swagger-uvprov.yml`.

### Running Tests

In order work/generate tests:
* use the command: `py.test tests` in the `uv-prov` folder
* coverage: `py.test --cov-report html --cov=uv-prov tests/` in the `uv-prov` folder
* generate cover report `py.test tests --html=build/test-report/index.html --self-contained-html` - this will generate a `build/test-report/index.html` folder that contains html based information about the tests coverage.
