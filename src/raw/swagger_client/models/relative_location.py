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

class RelativeLocation(object):
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
        'city': 'str',
        'state': 'str',
        'distance': 'QuantitativeValue',
        'bearing': 'QuantitativeValue'
    }

    attribute_map = {
        'city': 'city',
        'state': 'state',
        'distance': 'distance',
        'bearing': 'bearing'
    }

    def __init__(self, city=None, state=None, distance=None, bearing=None):  # noqa: E501
        """RelativeLocation - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._state = None
        self._distance = None
        self._bearing = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if distance is not None:
            self.distance = distance
        if bearing is not None:
            self.bearing = bearing

    @property
    def city(self):
        """Gets the city of this RelativeLocation.  # noqa: E501


        :return: The city of this RelativeLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this RelativeLocation.


        :param city: The city of this RelativeLocation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this RelativeLocation.  # noqa: E501


        :return: The state of this RelativeLocation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RelativeLocation.


        :param state: The state of this RelativeLocation.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def distance(self):
        """Gets the distance of this RelativeLocation.  # noqa: E501


        :return: The distance of this RelativeLocation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this RelativeLocation.


        :param distance: The distance of this RelativeLocation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._distance = distance

    @property
    def bearing(self):
        """Gets the bearing of this RelativeLocation.  # noqa: E501


        :return: The bearing of this RelativeLocation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._bearing

    @bearing.setter
    def bearing(self, bearing):
        """Sets the bearing of this RelativeLocation.


        :param bearing: The bearing of this RelativeLocation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._bearing = bearing

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
        if issubclass(RelativeLocation, dict):
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
        if not isinstance(other, RelativeLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
