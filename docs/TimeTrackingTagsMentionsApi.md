# timeular_api.TimeTrackingTagsMentionsApi

All URIs are relative to *https://api.timeular.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags_and_mentions**](TimeTrackingTagsMentionsApi.md#get_tags_and_mentions) | **GET** /tags-and-mentions | Fetch Tags &amp; Mentions


# **get_tags_and_mentions**
> TagsAndMentionsResponse get_tags_and_mentions(activity_id=activity_id)

Fetch Tags & Mentions

Tags and Mentions are created with the use of an explicit reference  with the Notes of your Time Entries / Tracking. Moreover, if an Activity is linked with Integration, let's say JIRA Project, JIRA task IDs are visible as Tags. With this endpoint, you can fetch all Tags and Mentions valid in context. Referring to a context means that Mentions are system-wide and  Tags are either bound to an Integration or to the Timeular System.

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
api_instance = timeular_api.TimeTrackingTagsMentionsApi(timeular_api.ApiClient(configuration))
activity_id = 'activity_id_example' # str | ID of an Activity, eg. `123` (optional)

try:
    # Fetch Tags & Mentions
    api_response = api_instance.get_tags_and_mentions(activity_id=activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingTagsMentionsApi->get_tags_and_mentions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| ID of an Activity, eg. &#x60;123&#x60; | [optional] 

### Return type

[**TagsAndMentionsResponse**](TagsAndMentionsResponse.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

