# timular_api.TimeTrackingCurrentTrackingApi

All URIs are relative to *https://api.timeular.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_tracking**](TimeTrackingCurrentTrackingApi.md#edit_tracking) | **PATCH** /tracking/{activityId} | Edit Tracking
[**get_current_tracking**](TimeTrackingCurrentTrackingApi.md#get_current_tracking) | **GET** /tracking | Show current Tracking
[**start_tracking**](TimeTrackingCurrentTrackingApi.md#start_tracking) | **POST** /tracking/{activityId}/start | Start Tracking
[**stop_tracking**](TimeTrackingCurrentTrackingApi.md#stop_tracking) | **POST** /tracking/{activityId}/stop | Stop Tracking


# **edit_tracking**
> EditTrackingResponse edit_tracking(activity_id, changed_note_of_a_tracking=changed_note_of_a_tracking)

Edit Tracking

With this endpoint, you can set/edit/remove Note of current Tracking. To remove a Note, just set the complete object to null and all values  within the object will be deleted too.

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
api_instance = timular_api.TimeTrackingCurrentTrackingApi(timular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity on which you are tracking time, eg. `123`
changed_note_of_a_tracking = timular_api.EditTrackingRequest() # EditTrackingRequest | changed note of a Tracking (optional)

try:
    # Edit Tracking
    api_response = api_instance.edit_tracking(activity_id, changed_note_of_a_tracking=changed_note_of_a_tracking)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCurrentTrackingApi->edit_tracking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity on which you are tracking time, eg. &#x60;123&#x60; | 
 **changed_note_of_a_tracking** | [**EditTrackingRequest**](EditTrackingRequest.md)| changed note of a Tracking | [optional] 

### Return type

[**EditTrackingResponse**](EditTrackingResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_tracking**
> CurrentTrackingResponse get_current_tracking()

Show current Tracking

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
api_instance = timular_api.TimeTrackingCurrentTrackingApi(timular_api.ApiClient(configuration))

try:
    # Show current Tracking
    api_response = api_instance.get_current_tracking()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCurrentTrackingApi->get_current_tracking: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentTrackingResponse**](CurrentTrackingResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_tracking**
> StartedTrackingResponse start_tracking(activity_id, start_timestamp_of_a_tracking=start_timestamp_of_a_tracking)

Start Tracking

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
api_instance = timular_api.TimeTrackingCurrentTrackingApi(timular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity on which you want to track time, eg. `123`
start_timestamp_of_a_tracking = timular_api.StartTrackingRequest() # StartTrackingRequest | start timestamp of a Tracking (optional)

try:
    # Start Tracking
    api_response = api_instance.start_tracking(activity_id, start_timestamp_of_a_tracking=start_timestamp_of_a_tracking)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCurrentTrackingApi->start_tracking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity on which you want to track time, eg. &#x60;123&#x60; | 
 **start_timestamp_of_a_tracking** | [**StartTrackingRequest**](StartTrackingRequest.md)| start timestamp of a Tracking | [optional] 

### Return type

[**StartedTrackingResponse**](StartedTrackingResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_tracking**
> StoppedTrackingResponse stop_tracking(activity_id, stop_timestamp_of_a_tracking=stop_timestamp_of_a_tracking)

Stop Tracking

With this endpoint, you can create a new Time Entry by stopping current time Tracking. Resulting Time Entry should have duration no shorter than 1 minute. The new Time Entry will be created even if it overlaps with other Time Entries  – in result existing Time Entries will be split or deleted in such manner,  that new one will fit without overlapping.

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
api_instance = timular_api.TimeTrackingCurrentTrackingApi(timular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity on which you are tracking time, eg. `123`
stop_timestamp_of_a_tracking = timular_api.StopTrackingRequest() # StopTrackingRequest | stop timestamp of a Tracking (optional)

try:
    # Stop Tracking
    api_response = api_instance.stop_tracking(activity_id, stop_timestamp_of_a_tracking=stop_timestamp_of_a_tracking)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCurrentTrackingApi->stop_tracking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity on which you are tracking time, eg. &#x60;123&#x60; | 
 **stop_timestamp_of_a_tracking** | [**StopTrackingRequest**](StopTrackingRequest.md)| stop timestamp of a Tracking | [optional] 

### Return type

[**StoppedTrackingResponse**](StoppedTrackingResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

