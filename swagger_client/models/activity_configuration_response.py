# coding: utf-8

"""
    Timeular Public API

     Welcome to the documentation of Timeular Public API v1.  You can try all requests here, in documentation, with use of `Try it out` button (available in each endpoint description after folding it out).  Most of endpoints are secured. In order to access them you have to provide *Access Token*. To do so, click on `Authorize` button below and provide `Bearer <your_access_token>` as a value for `Authorization` request header. To obtain *Access Token* you have to sign-in with pair of *API Key* and *API Secret* first. API Key & API Secret can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  **Warning:** authentication flow may change soon due to active development of Timeular and its API.  If you have any questions, please visit [Support page](http://support.timeular.com) and ask them there.  Happy API browsing!  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActivityConfigurationResponse(object):
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
        'id': 'str',
        'name': 'str',
        'color': 'str',
        'integration': 'str',
        'device_side': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'color': 'color',
        'integration': 'integration',
        'device_side': 'deviceSide'
    }

    def __init__(self, id=None, name=None, color=None, integration=None, device_side=None):  # noqa: E501
        """ActivityConfigurationResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._color = None
        self._integration = None
        self._device_side = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
        if integration is not None:
            self.integration = integration
        if device_side is not None:
            self.device_side = device_side

    @property
    def id(self):
        """Gets the id of this ActivityConfigurationResponse.  # noqa: E501


        :return: The id of this ActivityConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActivityConfigurationResponse.


        :param id: The id of this ActivityConfigurationResponse.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ActivityConfigurationResponse.  # noqa: E501


        :return: The name of this ActivityConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityConfigurationResponse.


        :param name: The name of this ActivityConfigurationResponse.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def color(self):
        """Gets the color of this ActivityConfigurationResponse.  # noqa: E501


        :return: The color of this ActivityConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ActivityConfigurationResponse.


        :param color: The color of this ActivityConfigurationResponse.  # noqa: E501
        :type: str
        """
        if color is not None and not re.search('(^[0-9abcdefABCDEF]{6}$)|(^[0-9abcdefABCDEF]{3}$)', color):  # noqa: E501
            raise ValueError("Invalid value for `color`, must be a follow pattern or equal to `/(^[0-9abcdefABCDEF]{6}$)|(^[0-9abcdefABCDEF]{3}$)/`")  # noqa: E501

        self._color = color

    @property
    def integration(self):
        """Gets the integration of this ActivityConfigurationResponse.  # noqa: E501


        :return: The integration of this ActivityConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this ActivityConfigurationResponse.


        :param integration: The integration of this ActivityConfigurationResponse.  # noqa: E501
        :type: str
        """
        if integration is not None and len(integration) < 1:
            raise ValueError("Invalid value for `integration`, length must be greater than or equal to `1`")  # noqa: E501

        self._integration = integration

    @property
    def device_side(self):
        """Gets the device_side of this ActivityConfigurationResponse.  # noqa: E501


        :return: The device_side of this ActivityConfigurationResponse.  # noqa: E501
        :rtype: int
        """
        return self._device_side

    @device_side.setter
    def device_side(self, device_side):
        """Sets the device_side of this ActivityConfigurationResponse.


        :param device_side: The device_side of this ActivityConfigurationResponse.  # noqa: E501
        :type: int
        """
        if device_side is not None and device_side < 0:  # noqa: E501
            raise ValueError("Invalid value for `device_side`, must be a value greater than or equal to `0`")  # noqa: E501

        self._device_side = device_side

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
        if not isinstance(other, ActivityConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other