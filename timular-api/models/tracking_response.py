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

from timular-api.models.tracking_activity_response import TrackingActivityResponse  # noqa: F401,E501


class TrackingResponse(object):
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
        'activity': 'TrackingActivityResponse',
        'started_at': 'str',
        'note': 'str'
    }

    attribute_map = {
        'activity': 'activity',
        'started_at': 'startedAt',
        'note': 'note'
    }

    def __init__(self, activity=None, started_at=None, note=None):  # noqa: E501
        """TrackingResponse - a model defined in Swagger"""  # noqa: E501

        self._activity = None
        self._started_at = None
        self._note = None
        self.discriminator = None

        if activity is not None:
            self.activity = activity
        if started_at is not None:
            self.started_at = started_at
        if note is not None:
            self.note = note

    @property
    def activity(self):
        """Gets the activity of this TrackingResponse.  # noqa: E501


        :return: The activity of this TrackingResponse.  # noqa: E501
        :rtype: TrackingActivityResponse
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this TrackingResponse.


        :param activity: The activity of this TrackingResponse.  # noqa: E501
        :type: TrackingActivityResponse
        """

        self._activity = activity

    @property
    def started_at(self):
        """Gets the started_at of this TrackingResponse.  # noqa: E501


        :return: The started_at of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this TrackingResponse.


        :param started_at: The started_at of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def note(self):
        """Gets the note of this TrackingResponse.  # noqa: E501


        :return: The note of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TrackingResponse.


        :param note: The note of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._note = note

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
        if not isinstance(other, TrackingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other