# coding: utf-8

"""
    Rosetta

    Build Once. Integrate Your Blockchain Everywhere.  # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.mempool_api import MempoolApi  # noqa: E501
from openapi_client.rest import ApiException


class TestMempoolApi(unittest.TestCase):
    """MempoolApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.mempool_api.MempoolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mempool(self):
        """Test case for mempool

        Get All Mempool Transactions  # noqa: E501
        """
        pass

    def test_mempool_transaction(self):
        """Test case for mempool_transaction

        Get a Mempool Transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()