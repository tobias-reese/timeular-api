# timeular_api.TimeTrackingActivitiesApi

All URIs are relative to *https://api.timeular.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_activity**](TimeTrackingActivitiesApi.md#archive_activity) | **DELETE** /activities/{activityId} | Archive an Activity
[**assign_activity_to_device_side**](TimeTrackingActivitiesApi.md#assign_activity_to_device_side) | **POST** /activities/{activityId}/device-side/{deviceSide} | Assign an Activity to Device Side
[**create_activity**](TimeTrackingActivitiesApi.md#create_activity) | **POST** /activities | Create an Activity
[**edit_activity**](TimeTrackingActivitiesApi.md#edit_activity) | **PATCH** /activities/{activityId} | Edit an Activity
[**get_activities**](TimeTrackingActivitiesApi.md#get_activities) | **GET** /activities | List all Activities
[**get_archived_activities**](TimeTrackingActivitiesApi.md#get_archived_activities) | **GET** /archived-activities | List all Archived Activities
[**unassign_activity_from_device_side**](TimeTrackingActivitiesApi.md#unassign_activity_from_device_side) | **DELETE** /activities/{activityId}/device-side/{deviceSide} | Unassign an Activity from a Device Side


# **archive_activity**
> SuccessWithIgnoredErrorsResponse archive_activity(activity_id)

Archive an Activity

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity, eg. `123`

try:
    # Archive an Activity
    api_response = api_instance.archive_activity(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->archive_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity, eg. &#x60;123&#x60; | 

### Return type

[**SuccessWithIgnoredErrorsResponse**](SuccessWithIgnoredErrorsResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_activity_to_device_side**
> ActivityConfigurationResponse assign_activity_to_device_side(activity_id, device_side)

Assign an Activity to Device Side

With this endpoint you can assign an Activity to any Side of your *active* Device. We do not know how many Sides does your Device have and which ones are valid (the default ZEI° has 8 sides numbered from 1 to 8). In order to activate your Device, make `POST` request to `/api/v2/devices/{deviceSerial}/active`.

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity, eg. `123`
device_side = 8.14 # float | Side of an active Device

try:
    # Assign an Activity to Device Side
    api_response = api_instance.assign_activity_to_device_side(activity_id, device_side)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->assign_activity_to_device_side: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity, eg. &#x60;123&#x60; | 
 **device_side** | **float**| Side of an active Device | 

### Return type

[**ActivityConfigurationResponse**](ActivityConfigurationResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity**
> ActivityConfigurationResponse create_activity(properties_of_a_new_activity=properties_of_a_new_activity)

Create an Activity

With this endpoint, you can create a new Activity. It should have name and color. A Name doesn't have to be unique. You can also, provide an Integration to which the Activity will belong to (`zei` is the default value, which means no special Integration). You can obtain list of enabled Integrations by making `GET` request to `/api/v2/integrations`.

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))
properties_of_a_new_activity = timeular_api.ActivityCreationRequest() # ActivityCreationRequest | properties of a new Activity (optional)

try:
    # Create an Activity
    api_response = api_instance.create_activity(properties_of_a_new_activity=properties_of_a_new_activity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->create_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **properties_of_a_new_activity** | [**ActivityCreationRequest**](ActivityCreationRequest.md)| properties of a new Activity | [optional] 

### Return type

[**ActivityConfigurationResponse**](ActivityConfigurationResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_activity**
> ActivityConfigurationResponse edit_activity(activity_id, properties_to_change=properties_to_change)

Edit an Activity

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity, eg. `123`
properties_to_change = timeular_api.ActivityEditionRequest() # ActivityEditionRequest | properties to change (optional)

try:
    # Edit an Activity
    api_response = api_instance.edit_activity(activity_id, properties_to_change=properties_to_change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->edit_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity, eg. &#x60;123&#x60; | 
 **properties_to_change** | [**ActivityEditionRequest**](ActivityEditionRequest.md)| properties to change | [optional] 

### Return type

[**ActivityConfigurationResponse**](ActivityConfigurationResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities**
> ActivitiesConfigurationResponse get_activities()

List all Activities

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))

try:
    # List all Activities
    api_response = api_instance.get_activities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->get_activities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActivitiesConfigurationResponse**](ActivitiesConfigurationResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archived_activities**
> ArchivedActivitiesResponse get_archived_activities()

List all Archived Activities

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))

try:
    # List all Archived Activities
    api_response = api_instance.get_archived_activities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->get_archived_activities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArchivedActivitiesResponse**](ArchivedActivitiesResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_activity_from_device_side**
> ActivityConfigurationResponse unassign_activity_from_device_side(activity_id, device_side)

Unassign an Activity from a Device Side

With this endpoint, you can delete an assignment of an Activity from a Side of  your active Device. In order to activate one proper Device, make a `POST`  request to `/api/v2/devices/{deviceSerial}/active`.

### Example
```python
from __future__ import print_function
import time
import timeular_api
from timeular_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = timeular_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timeular_api.TimeTrackingActivitiesApi(timeular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity, eg. `123`
device_side = 8.14 # float | Side of an active Device

try:
    # Unassign an Activity from a Device Side
    api_response = api_instance.unassign_activity_from_device_side(activity_id, device_side)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingActivitiesApi->unassign_activity_from_device_side: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity, eg. &#x60;123&#x60; | 
 **device_side** | **float**| Side of an active Device | 

### Return type

[**ActivityConfigurationResponse**](ActivityConfigurationResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

