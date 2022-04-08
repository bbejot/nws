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

class GeoJsonFeature(object):
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
        'id': 'str',
        'type': 'str',
        'geometry': 'GeoJsonGeometry',
        'properties': 'object'
    }

    attribute_map = {
        'context': '@context',
        'id': 'id',
        'type': 'type',
        'geometry': 'geometry',
        'properties': 'properties'
    }

    def __init__(self, context=None, id=None, type=None, geometry=None, properties=None):  # noqa: E501
        """GeoJsonFeature - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._geometry = None
        self._properties = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        self.type = type
        self.geometry = geometry
        self.properties = properties

    @property
    def context(self):
        """Gets the context of this GeoJsonFeature.  # noqa: E501


        :return: The context of this GeoJsonFeature.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this GeoJsonFeature.


        :param context: The context of this GeoJsonFeature.  # noqa: E501
        :type: JsonLdContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this GeoJsonFeature.  # noqa: E501


        :return: The id of this GeoJsonFeature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeoJsonFeature.


        :param id: The id of this GeoJsonFeature.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GeoJsonFeature.  # noqa: E501


        :return: The type of this GeoJsonFeature.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeoJsonFeature.


        :param type: The type of this GeoJsonFeature.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Feature"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def geometry(self):
        """Gets the geometry of this GeoJsonFeature.  # noqa: E501


        :return: The geometry of this GeoJsonFeature.  # noqa: E501
        :rtype: GeoJsonGeometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this GeoJsonFeature.


        :param geometry: The geometry of this GeoJsonFeature.  # noqa: E501
        :type: GeoJsonGeometry
        """
        self._geometry = geometry

    @property
    def properties(self):
        """Gets the properties of this GeoJsonFeature.  # noqa: E501


        :return: The properties of this GeoJsonFeature.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GeoJsonFeature.


        :param properties: The properties of this GeoJsonFeature.  # noqa: E501
        :type: object
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if issubclass(GeoJsonFeature, dict):
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
        if not isinstance(other, GeoJsonFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other