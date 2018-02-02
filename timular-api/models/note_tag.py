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


class NoteTag(object):
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
        'indices': 'list[int]',
        'key': 'str'
    }

    attribute_map = {
        'indices': 'indices',
        'key': 'key'
    }

    def __init__(self, indices=None, key=None):  # noqa: E501
        """NoteTag - a model defined in Swagger"""  # noqa: E501

        self._indices = None
        self._key = None
        self.discriminator = None

        if indices is not None:
            self.indices = indices
        if key is not None:
            self.key = key

    @property
    def indices(self):
        """Gets the indices of this NoteTag.  # noqa: E501


        :return: The indices of this NoteTag.  # noqa: E501
        :rtype: list[int]
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """Sets the indices of this NoteTag.


        :param indices: The indices of this NoteTag.  # noqa: E501
        :type: list[int]
        """

        self._indices = indices

    @property
    def key(self):
        """Gets the key of this NoteTag.  # noqa: E501


        :return: The key of this NoteTag.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NoteTag.


        :param key: The key of this NoteTag.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if not isinstance(other, NoteTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
