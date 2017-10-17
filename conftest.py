import alembic.config
import alembic.command
import falcon
import pytest
import sqlalchemy
import sqlalchemy.orm


@pytest.fixture
def app():
    application = falcon.API()
    application.req_options.auto_parse_form_urlencoded = True
    return application


@pytest.fixture(scope='session')
def default_route():
    return '/route'


@pytest.fixture(scope='session')
def db_connection_name():
    return 'sqlite:///'


@pytest.fixture(scope='session')
def db_schema(db_session_factory):
    _, _, connection = db_session_factory
    alembic_config = alembic.config.Config('alembic.ini')
    alembic_config.attributes['connection'] = connection
    alembic.command.upgrade(alembic_config, 'head')


@pytest.fixture(scope='session')
def db_session_factory(request, db_connection_name):
    engine = sqlalchemy.create_engine(db_connection_name)
    connection = engine.connect()
    transaction = connection.begin()

    session_factory = sqlalchemy.orm.sessionmaker(bind=connection)
    yield (session_factory, engine, connection)

    transaction.rollback()
    connection.close()


@pytest.fixture(scope='function')
def db_session(request, db_session_factory, db_schema):
    session_factory, _, _ = db_session_factory
    session = session_factory()
    yield session

    session.rollback()
    session.close()
