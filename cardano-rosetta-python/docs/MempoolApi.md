# openapi_client.MempoolApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mempool**](MempoolApi.md#mempool) | **POST** /mempool | Get All Mempool Transactions
[**mempool_transaction**](MempoolApi.md#mempool_transaction) | **POST** /mempool/transaction | Get a Mempool Transaction


# **mempool**
> MempoolResponse mempool(network_request)

Get All Mempool Transactions

Get all Transaction Identifiers in the mempool

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MempoolApi(api_client)
    network_request = openapi_client.NetworkRequest() # NetworkRequest | 

    try:
        # Get All Mempool Transactions
        api_response = api_instance.mempool(network_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MempoolApi->mempool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_request** | [**NetworkRequest**](NetworkRequest.md)|  | 

### Return type

[**MempoolResponse**](MempoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**500** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mempool_transaction**
> MempoolTransactionResponse mempool_transaction(mempool_transaction_request)

Get a Mempool Transaction

Get a transaction in the mempool by its Transaction Identifier. This is a separate request than fetching a block transaction (/block/transaction) because some blockchain nodes need to know that a transaction query is for something in the mempool instead of a transaction in a block. Transactions may not be fully parsable until they are in a block (ex: may not be possible to determine the fee to pay before a transaction is executed). On this endpoint, it is ok that returned transactions are only estimates of what may actually be included in a block.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MempoolApi(api_client)
    mempool_transaction_request = openapi_client.MempoolTransactionRequest() # MempoolTransactionRequest | 

    try:
        # Get a Mempool Transaction
        api_response = api_instance.mempool_transaction(mempool_transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MempoolApi->mempool_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mempool_transaction_request** | [**MempoolTransactionRequest**](MempoolTransactionRequest.md)|  | 

### Return type

[**MempoolTransactionResponse**](MempoolTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**500** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
