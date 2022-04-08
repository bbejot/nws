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

class TextProductLocationCollection(object):
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
        'context': 'JsonLdContext',
        'locations': 'dict(str, str)'
    }

    attribute_map = {
        'context': '@context',
        'locations': 'locations'
    }

    def __init__(self, context=None, locations=None):  # noqa: E501
        """TextProductLocationCollection - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._locations = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if locations is not None:
            self.locations = locations

    @property
    def context(self):
        """Gets the context of this TextProductLocationCollection.  # noqa: E501


        :return: The context of this TextProductLocationCollection.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this TextProductLocationCollection.


        :param context: The context of this TextProductLocationCollection.  # noqa: E501
        :type: JsonLdContext
        """

        self._context = context

    @property
    def locations(self):
        """Gets the locations of this TextProductLocationCollection.  # noqa: E501


        :return: The locations of this TextProductLocationCollection.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this TextProductLocationCollection.


        :param locations: The locations of this TextProductLocationCollection.  # noqa: E501
        :type: dict(str, str)
        """

        self._locations = locations

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
        if issubclass(TextProductLocationCollection, dict):
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
        if not isinstance(other, TextProductLocationCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other