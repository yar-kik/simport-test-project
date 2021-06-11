# Simporter Test Task (Junior PyDev)
[![Coverage Status](https://coveralls.io/repos/github/yar-kik/some-project/badge.svg?branch=master)](https://coveralls.io/github/yar-kik/some-project?branch=master)
[![Build Status](https://travis-ci.com/yar-kik/some-project.svg?branch=master)](https://travis-ci.com/yar-kik/some-project)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)

## Details
Source data is csv file containing following data:
* Event id (column id )
* Event timestamp (column timestamp )
* Several event attributes (columns asin, brand, etc )

You are expected to create two API methods:

1. `GET /api/info`

    Example:
    `http://localhost:5000/api/info`
    
    This method doesn’t require any parameters
    
    Returns: Information about possible filtering (list of attributes and list of values for each attribute)

2. `GET /api/timeline`

    Example:
    `http://localhost:5000/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=weekly&attr1=value1&attr2=value2`

### Parameters:
* startDate
* endDate
* Type (cumulative or usual)
* Grouping (weekly, bi-weekly or monthly)
* Filters (attributes and values)

### Grouping types:
You need to aggregate data during the period (from startDate to endDate):
* weekly (data for each week)
* bi - weekly (data for each 2 weeks)
* monthly (data for each month)

### Returns: 
JSON with timeline information according to input parameters:
Each point on the graph will be in a format:
* data type - dict:
    * keys data type - str
    * values data type - int (number of events during this period)

The response should have “timeline”(str) as a key, value - list of dicts with timeline data.

Example of response: `{“timeline”: [{“date”: “2019-01-01”, value: 10}, … ] }`

### Technical requirements
* Python 3.7+
* Flask
* Other details are up to you