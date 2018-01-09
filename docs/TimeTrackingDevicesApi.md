# timular-api.TimeTrackingDevicesApi

All URIs are relative to *https://api.timeular.com/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_device**](TimeTrackingDevicesApi.md#activate_device) | **POST** /devices/{deviceSerial}/active | Activate a Device
[**activate_device_0**](TimeTrackingDevicesApi.md#activate_device_0) | **PATCH** /devices/{deviceSerial} | Edit a Device
[**deactivate_device**](TimeTrackingDevicesApi.md#deactivate_device) | **DELETE** /devices/{deviceSerial}/active | Deactivate a Device
[**disable_device**](TimeTrackingDevicesApi.md#disable_device) | **POST** /devices/{deviceSerial}/disabled | Disable a Device
[**eanble_device**](TimeTrackingDevicesApi.md#eanble_device) | **DELETE** /devices/{deviceSerial}/disabled | Enable a Device
[**forget_device**](TimeTrackingDevicesApi.md#forget_device) | **DELETE** /devices/{deviceSerial} | Forget known Device
[**get_known_devices**](TimeTrackingDevicesApi.md#get_known_devices) | **GET** /devices | List all known Devices


# **activate_device**
> DeviceResponse activate_device(device_serial)

Activate a Device

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Activate a Device
    api_response = api_instance.activate_device(device_serial)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->activate_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_serial** | **str**| Serial number of a Device | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_device_0**
> DeviceResponse activate_device_0(device_serial, properties_to_change=properties_to_change)

Edit a Device

With this endpoint you can set name of your Device. Name is trimmed from leading and trailing whitespaces. You can remove name from a Device by setting it null/blank/empty.

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device
properties_to_change = timular-api.DeviceEditionRequest() # DeviceEditionRequest | properties to change (optional)

try:
    # Edit a Device
    api_response = api_instance.activate_device_0(device_serial, properties_to_change=properties_to_change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->activate_device_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_serial** | **str**| Serial number of a Device | 
 **properties_to_change** | [**DeviceEditionRequest**](DeviceEditionRequest.md)| properties to change | [optional] 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_device**
> DeviceResponse deactivate_device(device_serial)

Deactivate a Device

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Deactivate a Device
    api_response = api_instance.deactivate_device(device_serial)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->deactivate_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_serial** | **str**| Serial number of a Device | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_device**
> DeviceResponse disable_device(device_serial)

Disable a Device

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Disable a Device
    api_response = api_instance.disable_device(device_serial)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->disable_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_serial** | **str**| Serial number of a Device | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eanble_device**
> DeviceResponse eanble_device(device_serial)

Enable a Device

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Enable a Device
    api_response = api_instance.eanble_device(device_serial)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->eanble_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_serial** | **str**| Serial number of a Device | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forget_device**
> forget_device(device_serial)

Forget known Device

With this endpoint you can remove a Device from list of known Devices. In order to use it you have to make it active again with `POST` request to `/api/v1/devices/{deviceSerial}/active`.

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Forget known Device
    api_instance.forget_device(device_serial)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->forget_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_serial** | **str**| Serial number of a Device | 

### Return type

void (empty response body)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_known_devices**
> DevicesResponse get_known_devices()

List all known Devices

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
api_instance = timular-api.TimeTrackingDevicesApi(timular-api.ApiClient(configuration))

try:
    # List all known Devices
    api_response = api_instance.get_known_devices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->get_known_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesResponse**](DevicesResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

