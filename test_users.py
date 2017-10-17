
import pytest

import models
import users

@pytest.fixture
def users_create(app, default_route, db_session):
    handler = users.Create(db_session)
    app.add_route(default_route, handler)


def test_create(client, users_create, default_route, db_session):
    assert db_session.query(models.User).count() == 0
    client.post(default_route, data={})
    assert db_session.query(models.User).count() == 1
