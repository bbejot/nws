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
from swagger_client.models.observation_station import ObservationStation  # noqa: F401,E501

class ObservationStationJsonLd(ObservationStation):
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
        'geometry': 'GeometryString'
    }
    if hasattr(ObservationStation, "swagger_types"):
        swagger_types.update(ObservationStation.swagger_types)

    attribute_map = {
        'context': '@context',
        'geometry': 'geometry'
    }
    if hasattr(ObservationStation, "attribute_map"):
        attribute_map.update(ObservationStation.attribute_map)

    def __init__(self, context=None, geometry=None, *args, **kwargs):  # noqa: E501
        """ObservationStationJsonLd - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._geometry = None
        self.discriminator = None
        self.context = context
        self.geometry = geometry
        ObservationStation.__init__(self, *args, context=context, geometry=geometry, **kwargs)

    @property
    def context(self):
        """Gets the context of this ObservationStationJsonLd.  # noqa: E501


        :return: The context of this ObservationStationJsonLd.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ObservationStationJsonLd.


        :param context: The context of this ObservationStationJsonLd.  # noqa: E501
        :type: JsonLdContext
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def geometry(self):
        """Gets the geometry of this ObservationStationJsonLd.  # noqa: E501


        :return: The geometry of this ObservationStationJsonLd.  # noqa: E501
        :rtype: GeometryString
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this ObservationStationJsonLd.


        :param geometry: The geometry of this ObservationStationJsonLd.  # noqa: E501
        :type: GeometryString
        """
        if geometry is None:
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

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
        if issubclass(ObservationStationJsonLd, dict):
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
        if not isinstance(other, ObservationStationJsonLd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other