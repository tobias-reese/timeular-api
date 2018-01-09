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
from timular-api.api.time_tracking__devices_api import TimeTrackingDevicesApi  # noqa: E501
from timular-api.rest import ApiException


class TestTimeTrackingDevicesApi(unittest.TestCase):
    """TimeTrackingDevicesApi unit test stubs"""

    def setUp(self):
        self.api = timular-api.api.time_tracking__devices_api.TimeTrackingDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_device(self):
        """Test case for activate_device

        Activate a Device  # noqa: E501
        """
        pass

    def test_activate_device_0(self):
        """Test case for activate_device_0

        Edit a Device  # noqa: E501
        """
        pass

    def test_deactivate_device(self):
        """Test case for deactivate_device

        Deactivate a Device  # noqa: E501
        """
        pass

    def test_disable_device(self):
        """Test case for disable_device

        Disable a Device  # noqa: E501
        """
        pass

    def test_eanble_device(self):
        """Test case for eanble_device

        Enable a Device  # noqa: E501
        """
        pass

    def test_forget_device(self):
        """Test case for forget_device

        Forget known Device  # noqa: E501
        """
        pass

    def test_get_known_devices(self):
        """Test case for get_known_devices

        List all known Devices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
