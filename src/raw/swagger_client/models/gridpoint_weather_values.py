# coding: utf-8

"""
    weather.gov API

    weather.gov API  # noqa: E501

    OpenAPI spec version: 1.8.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GridpointWeatherValues(object):
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
        'valid_time': 'ISO8601Interval',
        'value': 'list[GridpointWeatherValue]'
    }

    attribute_map = {
        'valid_time': 'validTime',
        'value': 'value'
    }

    def __init__(self, valid_time=None, value=None):  # noqa: E501
        """GridpointWeatherValues - a model defined in Swagger"""  # noqa: E501
        self._valid_time = None
        self._value = None
        self.discriminator = None
        self.valid_time = valid_time
        self.value = value

    @property
    def valid_time(self):
        """Gets the valid_time of this GridpointWeatherValues.  # noqa: E501


        :return: The valid_time of this GridpointWeatherValues.  # noqa: E501
        :rtype: ISO8601Interval
        """
        return self._valid_time

    @valid_time.setter
    def valid_time(self, valid_time):
        """Sets the valid_time of this GridpointWeatherValues.


        :param valid_time: The valid_time of this GridpointWeatherValues.  # noqa: E501
        :type: ISO8601Interval
        """
        if valid_time is None:
            raise ValueError("Invalid value for `valid_time`, must not be `None`")  # noqa: E501

        self._valid_time = valid_time

    @property
    def value(self):
        """Gets the value of this GridpointWeatherValues.  # noqa: E501


        :return: The value of this GridpointWeatherValues.  # noqa: E501
        :rtype: list[GridpointWeatherValue]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GridpointWeatherValues.


        :param value: The value of this GridpointWeatherValues.  # noqa: E501
        :type: list[GridpointWeatherValue]
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(GridpointWeatherValues, dict):
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
        if not isinstance(other, GridpointWeatherValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
