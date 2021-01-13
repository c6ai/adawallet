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


class BlockResponse(object):
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
        'block': 'Block',
        'other_transactions': 'list[TransactionIdentifier]'
    }

    attribute_map = {
        'block': 'block',
        'other_transactions': 'other_transactions'
    }

    def __init__(self, block=None, other_transactions=None, local_vars_configuration=None):  # noqa: E501
        """BlockResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._block = None
        self._other_transactions = None
        self.discriminator = None

        self.block = block
        if other_transactions is not None:
            self.other_transactions = other_transactions

    @property
    def block(self):
        """Gets the block of this BlockResponse.  # noqa: E501


        :return: The block of this BlockResponse.  # noqa: E501
        :rtype: Block
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this BlockResponse.


        :param block: The block of this BlockResponse.  # noqa: E501
        :type: Block
        """
        if self.local_vars_configuration.client_side_validation and block is None:  # noqa: E501
            raise ValueError("Invalid value for `block`, must not be `None`")  # noqa: E501

        self._block = block

    @property
    def other_transactions(self):
        """Gets the other_transactions of this BlockResponse.  # noqa: E501

        Some blockchains may require additional transactions to be fetched that weren't returned in the block response (ex: block only returns transaction hashes). For blockchains with a lot of transactions in each block, this can be very useful as consumers can concurrently fetch all transactions returned.  # noqa: E501

        :return: The other_transactions of this BlockResponse.  # noqa: E501
        :rtype: list[TransactionIdentifier]
        """
        return self._other_transactions

    @other_transactions.setter
    def other_transactions(self, other_transactions):
        """Sets the other_transactions of this BlockResponse.

        Some blockchains may require additional transactions to be fetched that weren't returned in the block response (ex: block only returns transaction hashes). For blockchains with a lot of transactions in each block, this can be very useful as consumers can concurrently fetch all transactions returned.  # noqa: E501

        :param other_transactions: The other_transactions of this BlockResponse.  # noqa: E501
        :type: list[TransactionIdentifier]
        """

        self._other_transactions = other_transactions

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
        if not isinstance(other, BlockResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockResponse):
            return True

        return self.to_dict() != other.to_dict()