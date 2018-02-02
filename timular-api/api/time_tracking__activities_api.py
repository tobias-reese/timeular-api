# coding: utf-8

"""
    Timeular Public API

     Welcome to the documentation of Timeular Public API v2. If you want to have a look at the older and deprecated API v1 please just click on the following link: [Timeular Public API v1](./?v=v1)  You can try all requests here, in documentation, with use of `Try it out` button (available in each endpoint description after folding it out).  Most of endpoints are secured. In order to access them you have to provide *Access Token*. To do so, click on `Authorize` button below and provide `'Bearer *your_access_token*'` as a value for `Authorization` request header. To obtain *Access Token* you have to sign-in with pair of *API Key* and *API Secret* first. API Key & API Secret can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  **Warning:** authentication flow may change soon due to active development of Timeular and its API.  If you have any questions, please visit [Support page](http://support.timeular.com) and ask them there.  Happy API browsing!  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from timular-api.api_client import ApiClient


class TimeTrackingActivitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive_activity(self, activity_id, **kwargs):  # noqa: E501
        """Archive an Activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.archive_activity(activity_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :return: SuccessWithIgnoredErrorsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.archive_activity_with_http_info(activity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.archive_activity_with_http_info(activity_id, **kwargs)  # noqa: E501
            return data

    def archive_activity_with_http_info(self, activity_id, **kwargs):  # noqa: E501
        """Archive an Activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.archive_activity_with_http_info(activity_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :return: SuccessWithIgnoredErrorsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_activity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_id' is set
        if ('activity_id' not in params or
                params['activity_id'] is None):
            raise ValueError("Missing the required parameter `activity_id` when calling `archive_activity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_id' in params:
            path_params['activityId'] = params['activity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{activityId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessWithIgnoredErrorsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def assign_activity_to_device_side(self, activity_id, device_side, **kwargs):  # noqa: E501
        """Assign an Activity to Device Side  # noqa: E501

        With this endpoint you can assign an Activity to any Side of your *active* Device. We do not know how many Sides does your Device have and which ones are valid (the default ZEI° has 8 sides numbered from 1 to 8). In order to activate your Device, make `POST` request to `/api/v2/devices/{deviceSerial}/active`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.assign_activity_to_device_side(activity_id, device_side, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :param float device_side: Side of an active Device (required)
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.assign_activity_to_device_side_with_http_info(activity_id, device_side, **kwargs)  # noqa: E501
        else:
            (data) = self.assign_activity_to_device_side_with_http_info(activity_id, device_side, **kwargs)  # noqa: E501
            return data

    def assign_activity_to_device_side_with_http_info(self, activity_id, device_side, **kwargs):  # noqa: E501
        """Assign an Activity to Device Side  # noqa: E501

        With this endpoint you can assign an Activity to any Side of your *active* Device. We do not know how many Sides does your Device have and which ones are valid (the default ZEI° has 8 sides numbered from 1 to 8). In order to activate your Device, make `POST` request to `/api/v2/devices/{deviceSerial}/active`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.assign_activity_to_device_side_with_http_info(activity_id, device_side, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :param float device_side: Side of an active Device (required)
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_id', 'device_side']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method assign_activity_to_device_side" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_id' is set
        if ('activity_id' not in params or
                params['activity_id'] is None):
            raise ValueError("Missing the required parameter `activity_id` when calling `assign_activity_to_device_side`")  # noqa: E501
        # verify the required parameter 'device_side' is set
        if ('device_side' not in params or
                params['device_side'] is None):
            raise ValueError("Missing the required parameter `device_side` when calling `assign_activity_to_device_side`")  # noqa: E501

        if 'device_side' in params and params['device_side'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `device_side` when calling `assign_activity_to_device_side`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'activity_id' in params:
            path_params['activityId'] = params['activity_id']  # noqa: E501
        if 'device_side' in params:
            path_params['deviceSide'] = params['device_side']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{activityId}/device-side/{deviceSide}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityConfigurationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_activity(self, **kwargs):  # noqa: E501
        """Create an Activity  # noqa: E501

        With this endpoint, you can create a new Activity. It should have name and color. A Name doesn't have to be unique. You can also, provide an Integration to which the Activity will belong to (`zei` is the default value, which means no special Integration). You can obtain list of enabled Integrations by making `GET` request to `/api/v2/integrations`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_activity(async=True)
        >>> result = thread.get()

        :param async bool
        :param ActivityCreationRequest properties_of_a_new_activity: properties of a new Activity
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_activity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_activity_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_activity_with_http_info(self, **kwargs):  # noqa: E501
        """Create an Activity  # noqa: E501

        With this endpoint, you can create a new Activity. It should have name and color. A Name doesn't have to be unique. You can also, provide an Integration to which the Activity will belong to (`zei` is the default value, which means no special Integration). You can obtain list of enabled Integrations by making `GET` request to `/api/v2/integrations`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_activity_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param ActivityCreationRequest properties_of_a_new_activity: properties of a new Activity
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['properties_of_a_new_activity']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_activity" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'properties_of_a_new_activity' in params:
            body_params = params['properties_of_a_new_activity']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/activities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityConfigurationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_activity(self, activity_id, **kwargs):  # noqa: E501
        """Edit an Activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_activity(activity_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :param ActivityEditionRequest properties_to_change: properties to change
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.edit_activity_with_http_info(activity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_activity_with_http_info(activity_id, **kwargs)  # noqa: E501
            return data

    def edit_activity_with_http_info(self, activity_id, **kwargs):  # noqa: E501
        """Edit an Activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_activity_with_http_info(activity_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :param ActivityEditionRequest properties_to_change: properties to change
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_id', 'properties_to_change']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_activity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_id' is set
        if ('activity_id' not in params or
                params['activity_id'] is None):
            raise ValueError("Missing the required parameter `activity_id` when calling `edit_activity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_id' in params:
            path_params['activityId'] = params['activity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'properties_to_change' in params:
            body_params = params['properties_to_change']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{activityId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityConfigurationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_activities(self, **kwargs):  # noqa: E501
        """List all Activities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_activities(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ActivitiesConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_activities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_activities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_activities_with_http_info(self, **kwargs):  # noqa: E501
        """List all Activities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_activities_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ActivitiesConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivitiesConfigurationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_archived_activities(self, **kwargs):  # noqa: E501
        """List all Archived Activities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_archived_activities(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ArchivedActivitiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_archived_activities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_archived_activities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_archived_activities_with_http_info(self, **kwargs):  # noqa: E501
        """List all Archived Activities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_archived_activities_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ArchivedActivitiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_archived_activities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/archived-activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArchivedActivitiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unassign_activity_from_device_side(self, activity_id, device_side, **kwargs):  # noqa: E501
        """Unassign an Activity from a Device Side  # noqa: E501

        With this endpoint, you can delete an assignment of an Activity from a Side of  your active Device. In order to activate one proper Device, make a `POST`  request to `/api/v2/devices/{deviceSerial}/active`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.unassign_activity_from_device_side(activity_id, device_side, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :param float device_side: Side of an active Device (required)
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.unassign_activity_from_device_side_with_http_info(activity_id, device_side, **kwargs)  # noqa: E501
        else:
            (data) = self.unassign_activity_from_device_side_with_http_info(activity_id, device_side, **kwargs)  # noqa: E501
            return data

    def unassign_activity_from_device_side_with_http_info(self, activity_id, device_side, **kwargs):  # noqa: E501
        """Unassign an Activity from a Device Side  # noqa: E501

        With this endpoint, you can delete an assignment of an Activity from a Side of  your active Device. In order to activate one proper Device, make a `POST`  request to `/api/v2/devices/{deviceSerial}/active`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.unassign_activity_from_device_side_with_http_info(activity_id, device_side, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activity_id: ID of an Activity, eg. `123` (required)
        :param float device_side: Side of an active Device (required)
        :return: ActivityConfigurationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_id', 'device_side']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unassign_activity_from_device_side" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_id' is set
        if ('activity_id' not in params or
                params['activity_id'] is None):
            raise ValueError("Missing the required parameter `activity_id` when calling `unassign_activity_from_device_side`")  # noqa: E501
        # verify the required parameter 'device_side' is set
        if ('device_side' not in params or
                params['device_side'] is None):
            raise ValueError("Missing the required parameter `device_side` when calling `unassign_activity_from_device_side`")  # noqa: E501

        if 'device_side' in params and params['device_side'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `device_side` when calling `unassign_activity_from_device_side`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'activity_id' in params:
            path_params['activityId'] = params['activity_id']  # noqa: E501
        if 'device_side' in params:
            path_params['deviceSide'] = params['device_side']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationHeader']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{activityId}/device-side/{deviceSide}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityConfigurationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
