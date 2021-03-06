# coding: utf-8

"""
    HDL Testing Platform

    REST API for HDL TP  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ResponseDetails(object):
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
        'status': 'str',
        'message': 'str',
        'authorization': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'authorization': 'Authorization'
    }

    def __init__(self, status=None, message=None, authorization=None):  # noqa: E501
        """ResponseDetails - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._message = None
        self._authorization = None
        self.discriminator = None

        self.status = status
        self.message = message
        self.authorization = authorization

    @property
    def status(self):
        """Gets the status of this ResponseDetails.  # noqa: E501

        The status  # noqa: E501

        :return: The status of this ResponseDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseDetails.

        The status  # noqa: E501

        :param status: The status of this ResponseDetails.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this ResponseDetails.  # noqa: E501

        The message   # noqa: E501

        :return: The message of this ResponseDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseDetails.

        The message   # noqa: E501

        :param message: The message of this ResponseDetails.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def authorization(self):
        """Gets the authorization of this ResponseDetails.  # noqa: E501

        The JWT Auth Token   # noqa: E501

        :return: The authorization of this ResponseDetails.  # noqa: E501
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ResponseDetails.

        The JWT Auth Token   # noqa: E501

        :param authorization: The authorization of this ResponseDetails.  # noqa: E501
        :type: str
        """
        if authorization is None:
            raise ValueError("Invalid value for `authorization`, must not be `None`")  # noqa: E501

        self._authorization = authorization

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
        if issubclass(ResponseDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
