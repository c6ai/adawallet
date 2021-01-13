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


class AccountBalanceRequest(object):
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
        'network_identifier': 'NetworkIdentifier',
        'account_identifier': 'AccountIdentifier',
        'block_identifier': 'PartialBlockIdentifier'
    }

    attribute_map = {
        'network_identifier': 'network_identifier',
        'account_identifier': 'account_identifier',
        'block_identifier': 'block_identifier'
    }

    def __init__(self, network_identifier=None, account_identifier=None, block_identifier=None, local_vars_configuration=None):  # noqa: E501
        """AccountBalanceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network_identifier = None
        self._account_identifier = None
        self._block_identifier = None
        self.discriminator = None

        self.network_identifier = network_identifier
        self.account_identifier = account_identifier
        if block_identifier is not None:
            self.block_identifier = block_identifier

    @property
    def network_identifier(self):
        """Gets the network_identifier of this AccountBalanceRequest.  # noqa: E501


        :return: The network_identifier of this AccountBalanceRequest.  # noqa: E501
        :rtype: NetworkIdentifier
        """
        return self._network_identifier

    @network_identifier.setter
    def network_identifier(self, network_identifier):
        """Sets the network_identifier of this AccountBalanceRequest.


        :param network_identifier: The network_identifier of this AccountBalanceRequest.  # noqa: E501
        :type: NetworkIdentifier
        """
        if self.local_vars_configuration.client_side_validation and network_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `network_identifier`, must not be `None`")  # noqa: E501

        self._network_identifier = network_identifier

    @property
    def account_identifier(self):
        """Gets the account_identifier of this AccountBalanceRequest.  # noqa: E501


        :return: The account_identifier of this AccountBalanceRequest.  # noqa: E501
        :rtype: AccountIdentifier
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this AccountBalanceRequest.


        :param account_identifier: The account_identifier of this AccountBalanceRequest.  # noqa: E501
        :type: AccountIdentifier
        """
        if self.local_vars_configuration.client_side_validation and account_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def block_identifier(self):
        """Gets the block_identifier of this AccountBalanceRequest.  # noqa: E501


        :return: The block_identifier of this AccountBalanceRequest.  # noqa: E501
        :rtype: PartialBlockIdentifier
        """
        return self._block_identifier

    @block_identifier.setter
    def block_identifier(self, block_identifier):
        """Sets the block_identifier of this AccountBalanceRequest.


        :param block_identifier: The block_identifier of this AccountBalanceRequest.  # noqa: E501
        :type: PartialBlockIdentifier
        """

        self._block_identifier = block_identifier

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
        if not isinstance(other, AccountBalanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBalanceRequest):
            return True

        return self.to_dict() != other.to_dict()