
import pytest

import messages.findit_pb2
import models
import users

user_data = [
    {
        'name': '',
    },
    {
        'name': 'John Doe'
    }
]


@pytest.fixture(params=user_data)
def user_data(request):
    return request.param


@pytest.fixture
def users_create(app, default_route, db_session):
    handler = users.Create(db_session)
    app.add_route(default_route, handler)


def test_create(client, users_create, default_route, db_session, user_data):
    proto = messages.findit_pb2.CreateUserRequest()
    proto.name = user_data['name']

    assert db_session.query(models.User).count() == 0
    client.post(default_route, data=proto.SerializeToString())

    expected_number_of_users = user_data['name'] and 1 or 0
    assert db_session.query(models.User).count() == expected_number_of_users
