# timular-api.TimeTrackingReportsApi

All URIs are relative to *https://api.timeular.com/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_csv_report**](TimeTrackingReportsApi.md#generate_csv_report) | **GET** /report/{startTimestamp}/{stopTimestamp} | Generate CSV Report


# **generate_csv_report**
> generate_csv_report(start_timestamp, stop_timestamp, timezone)

Generate CSV Report

Generates Report in CSV which contains all the Time Entries from inside given time range. If some Time Entry exceeds report's time range, only matching part will be included.

### Example
```python
from __future__ import print_function
import time
import timular-api
from timular-api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular-api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular-api.TimeTrackingReportsApi(timular-api.ApiClient(configuration))
start_timestamp = 'start_timestamp_example' # str | eg. `2016-01-01T00:00:00.000`
stop_timestamp = 'stop_timestamp_example' # str | eg. `2017-12-31T23:59:59.999`
timezone = 'timezone_example' # str | Time-zone in which `StartDate` and `EndDate` columns will be shown, eg. `Europe/Berlin`. It honors Daylight Saving Time changes of given region. 

try:
    # Generate CSV Report
    api_instance.generate_csv_report(start_timestamp, stop_timestamp, timezone)
except ApiException as e:
    print("Exception when calling TimeTrackingReportsApi->generate_csv_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_timestamp** | **str**| eg. &#x60;2016-01-01T00:00:00.000&#x60; | 
 **stop_timestamp** | **str**| eg. &#x60;2017-12-31T23:59:59.999&#x60; | 
 **timezone** | **str**| Time-zone in which &#x60;StartDate&#x60; and &#x60;EndDate&#x60; columns will be shown, eg. &#x60;Europe/Berlin&#x60;. It honors Daylight Saving Time changes of given region.  | 

### Return type

void (empty response body)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain;charset=UTF-8, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

