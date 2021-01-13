# coding: utf-8

"""
    Rosetta

    Build Once. Integrate Your Blockchain Everywhere.  # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.account_balance_response import AccountBalanceResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestAccountBalanceResponse(unittest.TestCase):
    """AccountBalanceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountBalanceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.account_balance_response.AccountBalanceResponse()  # noqa: E501
        if include_optional :
            return AccountBalanceResponse(
                block_identifier = openapi_client.models.block_identifier.BlockIdentifier(
                    index = 1123941, 
                    hash = '0x1f2cc6c5027d2f201a5453ad1119574d2aed23a392654742ac3c78783c071f85', ), 
                balances = [
                    openapi_client.models.amount.Amount(
                        value = '1238089899992', 
                        currency = openapi_client.models.currency.Currency(
                            symbol = 'BTC', 
                            decimals = 8, 
                            metadata = {"Issuer":"Satoshi"}, ), 
                        metadata = openapi_client.models.metadata.metadata(), )
                    ], 
                coins = [
                    openapi_client.models.coin.Coin(
                        coin_identifier = openapi_client.models.coin_identifier.CoinIdentifier(
                            identifier = '0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1', ), 
                        amount = openapi_client.models.amount.Amount(
                            value = '1238089899992', 
                            currency = openapi_client.models.currency.Currency(
                                symbol = 'BTC', 
                                decimals = 8, 
                                metadata = {"Issuer":"Satoshi"}, ), 
                            metadata = openapi_client.models.metadata.metadata(), ), )
                    ], 
                metadata = {"sequence_number":23}
            )
        else :
            return AccountBalanceResponse(
                block_identifier = openapi_client.models.block_identifier.BlockIdentifier(
                    index = 1123941, 
                    hash = '0x1f2cc6c5027d2f201a5453ad1119574d2aed23a392654742ac3c78783c071f85', ),
                balances = [
                    openapi_client.models.amount.Amount(
                        value = '1238089899992', 
                        currency = openapi_client.models.currency.Currency(
                            symbol = 'BTC', 
                            decimals = 8, 
                            metadata = {"Issuer":"Satoshi"}, ), 
                        metadata = openapi_client.models.metadata.metadata(), )
                    ],
        )

    def testAccountBalanceResponse(self):
        """Test AccountBalanceResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()