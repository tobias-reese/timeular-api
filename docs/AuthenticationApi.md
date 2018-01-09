# timular-api.AuthenticationApi

All URIs are relative to *https://api.timeular.com/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_sign_in**](AuthenticationApi.md#developer_sign_in) | **POST** /developer/sign-in | Sign-in with API Key &amp; API Secret
[**get_api_key**](AuthenticationApi.md#get_api_key) | **GET** /developer/api-access | Fetch API Key
[**get_api_key_0**](AuthenticationApi.md#get_api_key_0) | **POST** /developer/api-access | Generate new API Key &amp; API Secret


# **developer_sign_in**
> DeveloperSignInResponse developer_sign_in(api_key_and_api_secret=api_key_and_api_secret)

Sign-in with API Key & API Secret

With this endpoint you can obtain Access Token required to access secured endpoints. To do so, you have to provide API Key & API Secret. They can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.

### Example
```python
from __future__ import print_function
import time
import timular-api
from timular-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timular-api.AuthenticationApi()
api_key_and_api_secret = timular-api.DeveloperSignInRequest() # DeveloperSignInRequest | API Key and API Secret (optional)

try:
    # Sign-in with API Key & API Secret
    api_response = api_instance.developer_sign_in(api_key_and_api_secret=api_key_and_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->developer_sign_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_and_api_secret** | [**DeveloperSignInRequest**](DeveloperSignInRequest.md)| API Key and API Secret | [optional] 

### Return type

[**DeveloperSignInResponse**](DeveloperSignInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> DeveloperApiAccessResponse get_api_key()

Fetch API Key

With this endpoint you can fetch your API Key (or `null` if you haven't generated any yet). You cannot obtain an API Secret in such way, because it's visible only once, after generation. If you have lost your API Secret, please generate a new pair of API Key & API Secret.

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
api_instance = timular-api.AuthenticationApi(timular-api.ApiClient(configuration))

try:
    # Fetch API Key
    api_response = api_instance.get_api_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_api_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeveloperApiAccessResponse**](DeveloperApiAccessResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_0**
> DeveloperFullApiAccessResponse get_api_key_0()

Generate new API Key & API Secret

With this endpoint you can generate new pair of API Key & API Secret. Every time you generate a new pair, an old one becomes invalid. Your API Secret won't be accessible later, so please note it down in some secret place. If you have lost your API Secret, you can generate a new pair of API Key & API Secret here.

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
api_instance = timular-api.AuthenticationApi(timular-api.ApiClient(configuration))

try:
    # Generate new API Key & API Secret
    api_response = api_instance.get_api_key_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_api_key_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeveloperFullApiAccessResponse**](DeveloperFullApiAccessResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

