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

class GeoJsonFeatureCollection(object):
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
        'type': 'str',
        'features': 'list[GeoJsonFeature]'
    }

    attribute_map = {
        'context': '@context',
        'type': 'type',
        'features': 'features'
    }

    def __init__(self, context=None, type=None, features=None):  # noqa: E501
        """GeoJsonFeatureCollection - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._type = None
        self._features = None
        self.discriminator = None
        if context is not None:
            self.context = context
        self.type = type
        self.features = features

    @property
    def context(self):
        """Gets the context of this GeoJsonFeatureCollection.  # noqa: E501


        :return: The context of this GeoJsonFeatureCollection.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this GeoJsonFeatureCollection.


        :param context: The context of this GeoJsonFeatureCollection.  # noqa: E501
        :type: JsonLdContext
        """

        self._context = context

    @property
    def type(self):
        """Gets the type of this GeoJsonFeatureCollection.  # noqa: E501


        :return: The type of this GeoJsonFeatureCollection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeoJsonFeatureCollection.


        :param type: The type of this GeoJsonFeatureCollection.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["FeatureCollection"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def features(self):
        """Gets the features of this GeoJsonFeatureCollection.  # noqa: E501


        :return: The features of this GeoJsonFeatureCollection.  # noqa: E501
        :rtype: list[GeoJsonFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this GeoJsonFeatureCollection.


        :param features: The features of this GeoJsonFeatureCollection.  # noqa: E501
        :type: list[GeoJsonFeature]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

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
        if issubclass(GeoJsonFeatureCollection, dict):
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
        if not isinstance(other, GeoJsonFeatureCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
