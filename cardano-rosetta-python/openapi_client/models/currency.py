# coding: utf-8

"""
    Rosetta

    Build Once. Integrate Your Blockchain Everywhere.  # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Currency(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'symbol': 'str',
        'decimals': 'int',
        'metadata': 'object'
    }

    attribute_map = {
        'symbol': 'symbol',
        'decimals': 'decimals',
        'metadata': 'metadata'
    }

    def __init__(self, symbol=None, decimals=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """Currency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._decimals = None
        self._metadata = None
        self.discriminator = None

        self.symbol = symbol
        self.decimals = decimals
        if metadata is not None:
            self.metadata = metadata

    @property
    def symbol(self):
        """Gets the symbol of this Currency.  # noqa: E501

        Canonical symbol associated with a currency.  # noqa: E501

        :return: The symbol of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Currency.

        Canonical symbol associated with a currency.  # noqa: E501

        :param symbol: The symbol of this Currency.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def decimals(self):
        """Gets the decimals of this Currency.  # noqa: E501

        Number of decimal places in the standard unit representation of the amount. For example, BTC has 8 decimals. Note that it is not possible to represent the value of some currency in atomic units that is not base 10.  # noqa: E501

        :return: The decimals of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this Currency.

        Number of decimal places in the standard unit representation of the amount. For example, BTC has 8 decimals. Note that it is not possible to represent the value of some currency in atomic units that is not base 10.  # noqa: E501

        :param decimals: The decimals of this Currency.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and decimals is None:  # noqa: E501
            raise ValueError("Invalid value for `decimals`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                decimals is not None and decimals < 0):  # noqa: E501
            raise ValueError("Invalid value for `decimals`, must be a value greater than or equal to `0`")  # noqa: E501

        self._decimals = decimals

    @property
    def metadata(self):
        """Gets the metadata of this Currency.  # noqa: E501

        Any additional information related to the currency itself. For example, it would be useful to populate this object with the contract address of an ERC-20 token.  # noqa: E501

        :return: The metadata of this Currency.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Currency.

        Any additional information related to the currency itself. For example, it would be useful to populate this object with the contract address of an ERC-20 token.  # noqa: E501

        :param metadata: The metadata of this Currency.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Currency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Currency):
            return True

        return self.to_dict() != other.to_dict()