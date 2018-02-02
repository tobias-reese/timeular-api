# timular_api.TimeTrackingDevicesApi

All URIs are relative to *https://api.timeular.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_device**](TimeTrackingDevicesApi.md#activate_device) | **POST** /devices/{deviceSerial}/active | Sets the status of a Device to active
[**deactivate_device**](TimeTrackingDevicesApi.md#deactivate_device) | **DELETE** /devices/{deviceSerial}/active | Removes the active status from the given Device
[**disable_device**](TimeTrackingDevicesApi.md#disable_device) | **POST** /devices/{deviceSerial}/disabled | Disable a Device
[**edit_device**](TimeTrackingDevicesApi.md#edit_device) | **PATCH** /devices/{deviceSerial} | Edit a Device
[**enable_device**](TimeTrackingDevicesApi.md#enable_device) | **DELETE** /devices/{deviceSerial}/disabled | Enable a Device
[**get_known_devices**](TimeTrackingDevicesApi.md#get_known_devices) | **GET** /devices | List all known Devices
[**remove_device**](TimeTrackingDevicesApi.md#remove_device) | **DELETE** /devices/{deviceSerial} | Remove known Device


# **activate_device**
> DeviceResponse activate_device(device_serial)

Sets the status of a Device to active

### Example
```python
from __future__ import print_function
import time
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Sets the status of a Device to active
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

# **deactivate_device**
> DeviceResponse deactivate_device(device_serial)

Removes the active status from the given Device

### Example
```python
from __future__ import print_function
import time
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Removes the active status from the given Device
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
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))
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

# **edit_device**
> DeviceResponse edit_device(device_serial, properties_to_change=properties_to_change)

Edit a Device

With this endpoint, you can set a name of your Device. The Name is trimmed automatically from leading and trailing whitespaces. You can remove name from a Device by setting it to the value null,  blank or empty.

### Example
```python
from __future__ import print_function
import time
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device
properties_to_change = timular_api.DeviceEditionRequest() # DeviceEditionRequest | properties to change (optional)

try:
    # Edit a Device
    api_response = api_instance.edit_device(device_serial, properties_to_change=properties_to_change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->edit_device: %s\n" % e)
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

# **enable_device**
> DeviceResponse enable_device(device_serial)

Enable a Device

### Example
```python
from __future__ import print_function
import time
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Enable a Device
    api_response = api_instance.enable_device(device_serial)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->enable_device: %s\n" % e)
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

# **get_known_devices**
> DevicesResponse get_known_devices()

List all known Devices

### Example
```python
from __future__ import print_function
import time
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))

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

# **remove_device**
> remove_device(device_serial)

Remove known Device

With this endpoint, you can remove a Device from list of known Devices. In order to remove the Device, you have to make it active again with `POST` request to `/api/v2//devices/{deviceSerial}/active`.

### Example
```python
from __future__ import print_function
import time
import timular_api
from timular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timular_api.TimeTrackingDevicesApi(timular_api.ApiClient(configuration))
device_serial = 'device_serial_example' # str | Serial number of a Device

try:
    # Remove known Device
    api_instance.remove_device(device_serial)
except ApiException as e:
    print("Exception when calling TimeTrackingDevicesApi->remove_device: %s\n" % e)
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

