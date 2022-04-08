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

class InlineResponse2002(object):
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
        'glossary': 'list[InlineResponse2002Glossary]'
    }

    attribute_map = {
        'context': '@context',
        'glossary': 'glossary'
    }

    def __init__(self, context=None, glossary=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._glossary = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if glossary is not None:
            self.glossary = glossary

    @property
    def context(self):
        """Gets the context of this InlineResponse2002.  # noqa: E501


        :return: The context of this InlineResponse2002.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this InlineResponse2002.


        :param context: The context of this InlineResponse2002.  # noqa: E501
        :type: JsonLdContext
        """

        self._context = context

    @property
    def glossary(self):
        """Gets the glossary of this InlineResponse2002.  # noqa: E501

        A list of glossary terms  # noqa: E501

        :return: The glossary of this InlineResponse2002.  # noqa: E501
        :rtype: list[InlineResponse2002Glossary]
        """
        return self._glossary

    @glossary.setter
    def glossary(self, glossary):
        """Sets the glossary of this InlineResponse2002.

        A list of glossary terms  # noqa: E501

        :param glossary: The glossary of this InlineResponse2002.  # noqa: E501
        :type: list[InlineResponse2002Glossary]
        """

        self._glossary = glossary

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
