import pytest
import falcon


@pytest.fixture
def app():
    application = falcon.API()
    application.req_options.auto_parse_form_urlencoded = True
    return application

@pytest.fixture
def default_route():
    return '/route'