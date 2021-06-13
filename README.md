# Simporter Test Task (Junior PyDev)
[![Coverage Status](https://coveralls.io/repos/github/yar-kik/simport-test-project/badge.svg?branch=master)](https://coveralls.io/github/yar-kik/simport-test-project?branch=master)
[![Build Status](https://travis-ci.com/yar-kik/simport-test-project.svg?branch=master)](https://travis-ci.com/yar-kik/simport-test-project)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)

## Used technologies
* Python 3.8
* Flask and Flask-Restful
* SQLite for development / Postgres for production environments
* Docker for containerizing
* Gunicorn and NGINX for production running

## How to run
Get local copy of project with: 
```
git clone https://github.com/yar-kik/simport-test-project.git
``` 

To build a local development environment and start API server run:  
```
docker-compose -f docker-compose-dev.yml up -d 
``` 
Or you can build a production ready environment: 
```
docker-compose -f docker-compose.yml up -d
``` 
This may take a few minutes. 
Finally, your api will work on `http://localhost:5000/` 
if you start development configuration or on `http://localhost/` if you start production 
configs.

With command line you can add test data from file and check work of API:
```
docker-compose exec api python add_test_data.py
```


## Available endpoints

1. `GET /api/info`

    Example:
    `http://localhost:5000/api/info`
    
    This method doesn’t require any parameters
    
    Returns: Information about possible filtering (list of attributes and list of values for each attribute)

2. `GET /api/timeline`

    Example:
    `http://localhost:5000/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=weekly&brand=Method&stars=5`
    
    Return number of events with specific filters and type.

### Parameters:
* startDate
* endDate
* Type (cumulative or usual)
* Grouping (weekly, bi-weekly or monthly)
* Filters (attributes and values). To get list of all available attributes and values use `GET /api/info` endpoint.

Example of response: `{“timeline”: [{“date”: “2019-01-01”, value: 10}, … ] }`