import httpretty

MOCK_URL = "https://example.com/"


def before_scenario(context, scenario):
    context.mock_url = MOCK_URL
    httpretty.enable()
    httpretty.register_uri(
        httpretty.GET,
        uri=context.mock_url,
        body='ok'
    )


def after_scenario(context, scenario):
    httpretty.disable()
