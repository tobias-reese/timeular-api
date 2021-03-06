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

from timeular_api.api_client import ApiClient


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def developer_sign_in(self, **kwargs):  # noqa: E501
        """Sign-in with API Key &amp; API Secret  # noqa: E501

        With this endpoint you can obtain Access Token required to access secured endpoints. To do so, you have to provide API Key & API Secret. They can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  If you possess your Access Token you can now add this inside an HTTP header field  `Authorization` as value `'Bearer *your_access_token*'` to access restricted endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.developer_sign_in(async=True)
        >>> result = thread.get()

        :param async bool
        :param DeveloperSignInRequest api_key_and_api_secret: API Key and API Secret
        :return: DeveloperSignInResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.developer_sign_in_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.developer_sign_in_with_http_info(**kwargs)  # noqa: E501
            return data

    def developer_sign_in_with_http_info(self, **kwargs):  # noqa: E501
        """Sign-in with API Key &amp; API Secret  # noqa: E501

        With this endpoint you can obtain Access Token required to access secured endpoints. To do so, you have to provide API Key & API Secret. They can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  If you possess your Access Token you can now add this inside an HTTP header field  `Authorization` as value `'Bearer *your_access_token*'` to access restricted endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.developer_sign_in_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param DeveloperSignInRequest api_key_and_api_secret: API Key and API Secret
        :return: DeveloperSignInResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key_and_api_secret']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method developer_sign_in" % key
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
        if 'api_key_and_api_secret' in params:
            body_params = params['api_key_and_api_secret']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/developer/sign-in', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeveloperSignInResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_api_key(self, **kwargs):  # noqa: E501
        """Generate new API Key &amp; API Secret  # noqa: E501

        With this endpoint you can generate a new pair of API Key & API Secret. Every time you generate a new pair, an old one becomes invalid. Your API Secret won't be accessible later, so please note it down in some secret place. If you have lost your API Secret, you can generate a new pair of API Key & API Secret here.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.generate_api_key(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DeveloperFullApiAccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.generate_api_key_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_api_key_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_api_key_with_http_info(self, **kwargs):  # noqa: E501
        """Generate new API Key &amp; API Secret  # noqa: E501

        With this endpoint you can generate a new pair of API Key & API Secret. Every time you generate a new pair, an old one becomes invalid. Your API Secret won't be accessible later, so please note it down in some secret place. If you have lost your API Secret, you can generate a new pair of API Key & API Secret here.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.generate_api_key_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DeveloperFullApiAccessResponse
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
                    " to method generate_api_key" % key
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
            '/developer/api-access', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeveloperFullApiAccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_key(self, **kwargs):  # noqa: E501
        """Fetch API Key  # noqa: E501

        With this endpoint you can fetch your API Key (or `null` if you haven't generated any yet). You cannot obtain an API Secret in such way, because it's visible only once, after generation. If you have lost your API Secret, please generate a new pair of API Key & API Secret.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_api_key(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DeveloperApiAccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_api_key_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_key_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_key_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch API Key  # noqa: E501

        With this endpoint you can fetch your API Key (or `null` if you haven't generated any yet). You cannot obtain an API Secret in such way, because it's visible only once, after generation. If you have lost your API Secret, please generate a new pair of API Key & API Secret.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_api_key_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DeveloperApiAccessResponse
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
                    " to method get_api_key" % key
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
            '/developer/api-access', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeveloperApiAccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
