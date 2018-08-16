import httpretty
import requests
from behave import given, when, then
from nose.tools import assert_in

import requestsdefaulter


@given(u'I have the default headers set to')
def set_default_headers(context):
    """
       :type context: behave.runner.Context
    """
    headers = row_table(context)

    def default_headers_function():
        return headers

    requestsdefaulter.default_headers(default_headers_function)


def row_table(context):
    headers = {}
    for row in context.table:
        headers[row["Header"]] = row["Value"]
    return headers


@when(u'I make a request')
def make_request(context):
    """
       :type context: behave.runner.Context
    """
    requests.get(context.mock_url)


@then(u'the request should contain the headers')
def assert_headers(context):
    """
       :type context: behave.runner.Context
    """
    expected_headers = [(k, v) for k, v in row_table(context).items()]
    request = httpretty.last_request()
    actual_headers = request.headers.items()

    for expected_header in expected_headers:
        assert_in(expected_header, actual_headers)


@when(u'I make a request with the headers')
def make_request_with_headers(context):
    """
       :type context: behave.runner.Context
    """
    headers = row_table(context)
    requests.get(context.mock_url, headers=headers)
