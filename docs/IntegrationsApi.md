# timular-api.IntegrationsApi

All URIs are relative to *https://api.timeular.com/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /integrations | List enabled Integrations


# **get_integration**
> IntegrationsResponse get_integration()

List enabled Integrations

With this endpoint you can list names of all Integrations you have enabled on [Profile website](https://profile.timeular.com/#/app/integrations).

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
api_instance = timular-api.IntegrationsApi(timular-api.ApiClient(configuration))

try:
    # List enabled Integrations
    api_response = api_instance.get_integration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntegrationsResponse**](IntegrationsResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

