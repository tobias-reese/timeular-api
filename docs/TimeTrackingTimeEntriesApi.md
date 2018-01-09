# swagger_client.TimeTrackingTimeEntriesApi

All URIs are relative to *https://api.timeular.com/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_entry**](TimeTrackingTimeEntriesApi.md#create_time_entry) | **POST** /time-entries | Create Time Entry
[**delete_time_entry**](TimeTrackingTimeEntriesApi.md#delete_time_entry) | **DELETE** /time-entries/{timeEntryId} | Delete a Time Entry
[**edit_time_entry**](TimeTrackingTimeEntriesApi.md#edit_time_entry) | **PATCH** /time-entries/{timeEntryId} | Edit a Time Entry
[**get_time_entries_in_range**](TimeTrackingTimeEntriesApi.md#get_time_entries_in_range) | **GET** /time-entries/{stoppedAfter}/{startedBefore} | Find Time Entries in given range
[**get_time_entry**](TimeTrackingTimeEntriesApi.md#get_time_entry) | **GET** /time-entries/{timeEntryId} | Find Time Entry by its ID


# **create_time_entry**
> TimeEntryResponse create_time_entry(properties_of_a_new_time_entry=properties_of_a_new_time_entry)

Create Time Entry

With this endpoint you can create a new Time Entry. It should be connected to an Activity and have duration no shorter than 1 minute. Note can be provided too, but it's not required. You can provide one or more Tags and Mentions in a Note, each of them prefixed with `#` or `@`. If related Activity is bound to some Integration, let's say JIRA Project, JIRA task IDs is a valid Tag too. Time Entry will be created even if it overlaps with other Time Entries – in result existing Time Entries will be split or deleted in such manner, that new one will fit without overlapping.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TimeTrackingTimeEntriesApi(swagger_client.ApiClient(configuration))
properties_of_a_new_time_entry = swagger_client.TimeEntryCreationRequest() # TimeEntryCreationRequest | properties of a new Time Entry (optional)

try:
    # Create Time Entry
    api_response = api_instance.create_time_entry(properties_of_a_new_time_entry=properties_of_a_new_time_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingTimeEntriesApi->create_time_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **properties_of_a_new_time_entry** | [**TimeEntryCreationRequest**](TimeEntryCreationRequest.md)| properties of a new Time Entry | [optional] 

### Return type

[**TimeEntryResponse**](TimeEntryResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_entry**
> SuccessWithIgnoredErrorsResponse delete_time_entry(time_entry_id)

Delete a Time Entry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TimeTrackingTimeEntriesApi(swagger_client.ApiClient(configuration))
time_entry_id = 'time_entry_id_example' # str | ID of an Activity, eg. `987`

try:
    # Delete a Time Entry
    api_response = api_instance.delete_time_entry(time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingTimeEntriesApi->delete_time_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**| ID of an Activity, eg. &#x60;987&#x60; | 

### Return type

[**SuccessWithIgnoredErrorsResponse**](SuccessWithIgnoredErrorsResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_time_entry**
> TimeEntryResponse edit_time_entry(time_entry_id, properties_to_change=properties_to_change)

Edit a Time Entry

With this endpoint you can edit existing Time Entry. When changing Activity ID please note, that both new and old Activity attached to Time Entry have to belong to same Integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TimeTrackingTimeEntriesApi(swagger_client.ApiClient(configuration))
time_entry_id = 'time_entry_id_example' # str | ID of an Activity, eg. `987`
properties_to_change = swagger_client.TimeEntryEditionRequest() # TimeEntryEditionRequest | properties to change (optional)

try:
    # Edit a Time Entry
    api_response = api_instance.edit_time_entry(time_entry_id, properties_to_change=properties_to_change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingTimeEntriesApi->edit_time_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**| ID of an Activity, eg. &#x60;987&#x60; | 
 **properties_to_change** | [**TimeEntryEditionRequest**](TimeEntryEditionRequest.md)| properties to change | [optional] 

### Return type

[**TimeEntryResponse**](TimeEntryResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_entries_in_range**
> TimeEntriesResponse get_time_entries_in_range(stopped_after, started_before)

Find Time Entries in given range

Find Time Entries which have at least one millisecond in common with provided time range.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TimeTrackingTimeEntriesApi(swagger_client.ApiClient(configuration))
stopped_after = 'stopped_after_example' # str | Timestamp which matches all Time Entries stopped after it. Eg. `2017-01-01T00:00:00.000`.
started_before = 'started_before_example' # str | Timestamp which matches all Time Entries started before it. Eg. `2017-12-31T23:59:59.999`.

try:
    # Find Time Entries in given range
    api_response = api_instance.get_time_entries_in_range(stopped_after, started_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingTimeEntriesApi->get_time_entries_in_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopped_after** | **str**| Timestamp which matches all Time Entries stopped after it. Eg. &#x60;2017-01-01T00:00:00.000&#x60;. | 
 **started_before** | **str**| Timestamp which matches all Time Entries started before it. Eg. &#x60;2017-12-31T23:59:59.999&#x60;. | 

### Return type

[**TimeEntriesResponse**](TimeEntriesResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_entry**
> TimeEntryResponse get_time_entry(time_entry_id)

Find Time Entry by its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TimeTrackingTimeEntriesApi(swagger_client.ApiClient(configuration))
time_entry_id = 'time_entry_id_example' # str | ID of an Activity, eg. `987`

try:
    # Find Time Entry by its ID
    api_response = api_instance.get_time_entry(time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingTimeEntriesApi->get_time_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**| ID of an Activity, eg. &#x60;987&#x60; | 

### Return type

[**TimeEntryResponse**](TimeEntryResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

