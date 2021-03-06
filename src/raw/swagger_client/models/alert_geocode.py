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

class AlertGeocode(object):
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
        'ugc': 'list[NWSZoneID]',
        'same': 'list[str]'
    }

    attribute_map = {
        'ugc': 'UGC',
        'same': 'SAME'
    }

    def __init__(self, ugc=None, same=None):  # noqa: E501
        """AlertGeocode - a model defined in Swagger"""  # noqa: E501
        self._ugc = None
        self._same = None
        self.discriminator = None
        if ugc is not None:
            self.ugc = ugc
        if same is not None:
            self.same = same

    @property
    def ugc(self):
        """Gets the ugc of this AlertGeocode.  # noqa: E501

        A list of NWS public zone or county identifiers.  # noqa: E501

        :return: The ugc of this AlertGeocode.  # noqa: E501
        :rtype: list[NWSZoneID]
        """
        return self._ugc

    @ugc.setter
    def ugc(self, ugc):
        """Sets the ugc of this AlertGeocode.

        A list of NWS public zone or county identifiers.  # noqa: E501

        :param ugc: The ugc of this AlertGeocode.  # noqa: E501
        :type: list[NWSZoneID]
        """

        self._ugc = ugc

    @property
    def same(self):
        """Gets the same of this AlertGeocode.  # noqa: E501

        A list of SAME (Specific Area Message Encoding) codes for affected counties.  # noqa: E501

        :return: The same of this AlertGeocode.  # noqa: E501
        :rtype: list[str]
        """
        return self._same

    @same.setter
    def same(self, same):
        """Sets the same of this AlertGeocode.

        A list of SAME (Specific Area Message Encoding) codes for affected counties.  # noqa: E501

        :param same: The same of this AlertGeocode.  # noqa: E501
        :type: list[str]
        """

        self._same = same

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
        if issubclass(AlertGeocode, dict):
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
        if not isinstance(other, AlertGeocode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
