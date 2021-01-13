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


class AccountIdentifier(object):
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
        'address': 'str',
        'sub_account': 'SubAccountIdentifier',
        'metadata': 'object'
    }

    attribute_map = {
        'address': 'address',
        'sub_account': 'sub_account',
        'metadata': 'metadata'
    }

    def __init__(self, address=None, sub_account=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """AccountIdentifier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._sub_account = None
        self._metadata = None
        self.discriminator = None

        self.address = address
        if sub_account is not None:
            self.sub_account = sub_account
        if metadata is not None:
            self.metadata = metadata

    @property
    def address(self):
        """Gets the address of this AccountIdentifier.  # noqa: E501

        The address may be a cryptographic public key (or some encoding of it) or a provided username.  # noqa: E501

        :return: The address of this AccountIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccountIdentifier.

        The address may be a cryptographic public key (or some encoding of it) or a provided username.  # noqa: E501

        :param address: The address of this AccountIdentifier.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def sub_account(self):
        """Gets the sub_account of this AccountIdentifier.  # noqa: E501


        :return: The sub_account of this AccountIdentifier.  # noqa: E501
        :rtype: SubAccountIdentifier
        """
        return self._sub_account

    @sub_account.setter
    def sub_account(self, sub_account):
        """Sets the sub_account of this AccountIdentifier.


        :param sub_account: The sub_account of this AccountIdentifier.  # noqa: E501
        :type: SubAccountIdentifier
        """

        self._sub_account = sub_account

    @property
    def metadata(self):
        """Gets the metadata of this AccountIdentifier.  # noqa: E501

        Blockchains that utilize a username model (where the address is not a derivative of a cryptographic public key) should specify the public key(s) owned by the address in metadata.  # noqa: E501

        :return: The metadata of this AccountIdentifier.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AccountIdentifier.

        Blockchains that utilize a username model (where the address is not a derivative of a cryptographic public key) should specify the public key(s) owned by the address in metadata.  # noqa: E501

        :param metadata: The metadata of this AccountIdentifier.  # noqa: E501
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
        if not isinstance(other, AccountIdentifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountIdentifier):
            return True

        return self.to_dict() != other.to_dict()