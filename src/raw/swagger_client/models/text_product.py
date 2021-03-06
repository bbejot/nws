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

class TextProduct(object):
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
        'id': 'str',
        'wmo_collective_id': 'str',
        'issuing_office': 'str',
        'issuance_time': 'datetime',
        'product_code': 'str',
        'product_name': 'str',
        'product_text': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'id': 'id',
        'wmo_collective_id': 'wmoCollectiveId',
        'issuing_office': 'issuingOffice',
        'issuance_time': 'issuanceTime',
        'product_code': 'productCode',
        'product_name': 'productName',
        'product_text': 'productText'
    }

    def __init__(self, context=None, id=None, wmo_collective_id=None, issuing_office=None, issuance_time=None, product_code=None, product_name=None, product_text=None):  # noqa: E501
        """TextProduct - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._id = None
        self._wmo_collective_id = None
        self._issuing_office = None
        self._issuance_time = None
        self._product_code = None
        self._product_name = None
        self._product_text = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if id is not None:
            self.id = id
        if wmo_collective_id is not None:
            self.wmo_collective_id = wmo_collective_id
        if issuing_office is not None:
            self.issuing_office = issuing_office
        if issuance_time is not None:
            self.issuance_time = issuance_time
        if product_code is not None:
            self.product_code = product_code
        if product_name is not None:
            self.product_name = product_name
        if product_text is not None:
            self.product_text = product_text

    @property
    def context(self):
        """Gets the context of this TextProduct.  # noqa: E501


        :return: The context of this TextProduct.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this TextProduct.


        :param context: The context of this TextProduct.  # noqa: E501
        :type: JsonLdContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this TextProduct.  # noqa: E501


        :return: The id of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TextProduct.


        :param id: The id of this TextProduct.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id(self):
        """Gets the id of this TextProduct.  # noqa: E501


        :return: The id of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TextProduct.


        :param id: The id of this TextProduct.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wmo_collective_id(self):
        """Gets the wmo_collective_id of this TextProduct.  # noqa: E501


        :return: The wmo_collective_id of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._wmo_collective_id

    @wmo_collective_id.setter
    def wmo_collective_id(self, wmo_collective_id):
        """Sets the wmo_collective_id of this TextProduct.


        :param wmo_collective_id: The wmo_collective_id of this TextProduct.  # noqa: E501
        :type: str
        """

        self._wmo_collective_id = wmo_collective_id

    @property
    def issuing_office(self):
        """Gets the issuing_office of this TextProduct.  # noqa: E501


        :return: The issuing_office of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._issuing_office

    @issuing_office.setter
    def issuing_office(self, issuing_office):
        """Sets the issuing_office of this TextProduct.


        :param issuing_office: The issuing_office of this TextProduct.  # noqa: E501
        :type: str
        """

        self._issuing_office = issuing_office

    @property
    def issuance_time(self):
        """Gets the issuance_time of this TextProduct.  # noqa: E501


        :return: The issuance_time of this TextProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._issuance_time

    @issuance_time.setter
    def issuance_time(self, issuance_time):
        """Sets the issuance_time of this TextProduct.


        :param issuance_time: The issuance_time of this TextProduct.  # noqa: E501
        :type: datetime
        """

        self._issuance_time = issuance_time

    @property
    def product_code(self):
        """Gets the product_code of this TextProduct.  # noqa: E501


        :return: The product_code of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this TextProduct.


        :param product_code: The product_code of this TextProduct.  # noqa: E501
        :type: str
        """

        self._product_code = product_code

    @property
    def product_name(self):
        """Gets the product_name of this TextProduct.  # noqa: E501


        :return: The product_name of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this TextProduct.


        :param product_name: The product_name of this TextProduct.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_text(self):
        """Gets the product_text of this TextProduct.  # noqa: E501


        :return: The product_text of this TextProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_text

    @product_text.setter
    def product_text(self, product_text):
        """Sets the product_text of this TextProduct.


        :param product_text: The product_text of this TextProduct.  # noqa: E501
        :type: str
        """

        self._product_text = product_text

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
        if issubclass(TextProduct, dict):
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
        if not isinstance(other, TextProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
