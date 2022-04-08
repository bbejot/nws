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

class QuantitativeValue(object):
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
        'value': 'float',
        'max_value': 'float',
        'min_value': 'float',
        'unit_code': 'UnitOfMeasure',
        'quality_control': 'str'
    }

    attribute_map = {
        'value': 'value',
        'max_value': 'maxValue',
        'min_value': 'minValue',
        'unit_code': 'unitCode',
        'quality_control': 'qualityControl'
    }

    def __init__(self, value=None, max_value=None, min_value=None, unit_code=None, quality_control=None):  # noqa: E501
        """QuantitativeValue - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._max_value = None
        self._min_value = None
        self._unit_code = None
        self._quality_control = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if unit_code is not None:
            self.unit_code = unit_code
        if quality_control is not None:
            self.quality_control = quality_control

    @property
    def value(self):
        """Gets the value of this QuantitativeValue.  # noqa: E501

        A measured value  # noqa: E501

        :return: The value of this QuantitativeValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this QuantitativeValue.

        A measured value  # noqa: E501

        :param value: The value of this QuantitativeValue.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def max_value(self):
        """Gets the max_value of this QuantitativeValue.  # noqa: E501

        The maximum value of a range of measured values  # noqa: E501

        :return: The max_value of this QuantitativeValue.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this QuantitativeValue.

        The maximum value of a range of measured values  # noqa: E501

        :param max_value: The max_value of this QuantitativeValue.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this QuantitativeValue.  # noqa: E501

        The minimum value of a range of measured values  # noqa: E501

        :return: The min_value of this QuantitativeValue.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this QuantitativeValue.

        The minimum value of a range of measured values  # noqa: E501

        :param min_value: The min_value of this QuantitativeValue.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def unit_code(self):
        """Gets the unit_code of this QuantitativeValue.  # noqa: E501


        :return: The unit_code of this QuantitativeValue.  # noqa: E501
        :rtype: UnitOfMeasure
        """
        return self._unit_code

    @unit_code.setter
    def unit_code(self, unit_code):
        """Sets the unit_code of this QuantitativeValue.


        :param unit_code: The unit_code of this QuantitativeValue.  # noqa: E501
        :type: UnitOfMeasure
        """

        self._unit_code = unit_code

    @property
    def quality_control(self):
        """Gets the quality_control of this QuantitativeValue.  # noqa: E501

        For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml   # noqa: E501

        :return: The quality_control of this QuantitativeValue.  # noqa: E501
        :rtype: str
        """
        return self._quality_control

    @quality_control.setter
    def quality_control(self, quality_control):
        """Sets the quality_control of this QuantitativeValue.

        For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml   # noqa: E501

        :param quality_control: The quality_control of this QuantitativeValue.  # noqa: E501
        :type: str
        """
        allowed_values = ["Z", "C", "S", "V", "X", "Q", "G", "B", "T"]  # noqa: E501
        if quality_control not in allowed_values:
            raise ValueError(
                "Invalid value for `quality_control` ({0}), must be one of {1}"  # noqa: E501
                .format(quality_control, allowed_values)
            )

        self._quality_control = quality_control

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
        if issubclass(QuantitativeValue, dict):
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
        if not isinstance(other, QuantitativeValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
