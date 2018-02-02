# coding: utf-8

"""
    Timeular Public API

     Welcome to the documentation of Timeular Public API v2. If you want to have a look at the older and deprecated API v1 please just click on the following link: [Timeular Public API v1](./?v=v1)  You can try all requests here, in documentation, with use of `Try it out` button (available in each endpoint description after folding it out).  Most of endpoints are secured. In order to access them you have to provide *Access Token*. To do so, click on `Authorize` button below and provide `'Bearer *your_access_token*'` as a value for `Authorization` request header. To obtain *Access Token* you have to sign-in with pair of *API Key* and *API Secret* first. API Key & API Secret can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  **Warning:** authentication flow may change soon due to active development of Timeular and its API.  If you have any questions, please visit [Support page](http://support.timeular.com) and ask them there.  Happy API browsing!  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'serial': 'str',
        'name': 'str',
        'active': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'serial': 'serial',
        'name': 'name',
        'active': 'active',
        'disabled': 'disabled'
    }

    def __init__(self, serial=None, name=None, active=None, disabled=None):  # noqa: E501
        """DeviceResponse - a model defined in Swagger"""  # noqa: E501

        self._serial = None
        self._name = None
        self._active = None
        self._disabled = None
        self.discriminator = None

        if serial is not None:
            self.serial = serial
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if disabled is not None:
            self.disabled = disabled

    @property
    def serial(self):
        """Gets the serial of this DeviceResponse.  # noqa: E501


        :return: The serial of this DeviceResponse.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeviceResponse.


        :param serial: The serial of this DeviceResponse.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def name(self):
        """Gets the name of this DeviceResponse.  # noqa: E501


        :return: The name of this DeviceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceResponse.


        :param name: The name of this DeviceResponse.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def active(self):
        """Gets the active of this DeviceResponse.  # noqa: E501


        :return: The active of this DeviceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DeviceResponse.


        :param active: The active of this DeviceResponse.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def disabled(self):
        """Gets the disabled of this DeviceResponse.  # noqa: E501


        :return: The disabled of this DeviceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this DeviceResponse.


        :param disabled: The disabled of this DeviceResponse.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
