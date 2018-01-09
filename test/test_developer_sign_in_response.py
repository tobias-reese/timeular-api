# coding: utf-8

"""
    Timeular Public API

     Welcome to the documentation of Timeular Public API v1.  You can try all requests here, in documentation, with use of `Try it out` button (available in each endpoint description after folding it out).  Most of endpoints are secured. In order to access them you have to provide *Access Token*. To do so, click on `Authorize` button below and provide `Bearer <your_access_token>` as a value for `Authorization` request header. To obtain *Access Token* you have to sign-in with pair of *API Key* and *API Secret* first. API Key & API Secret can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  **Warning:** authentication flow may change soon due to active development of Timeular and its API.  If you have any questions, please visit [Support page](http://support.timeular.com) and ask them there.  Happy API browsing!  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import timular-api
from timular-api.models.developer_sign_in_response import DeveloperSignInResponse  # noqa: E501
from timular-api.rest import ApiException


class TestDeveloperSignInResponse(unittest.TestCase):
    """DeveloperSignInResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeveloperSignInResponse(self):
        """Test DeveloperSignInResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = timular-api.models.developer_sign_in_response.DeveloperSignInResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
