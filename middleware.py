import sqlalchemy
import sqlalchemy.orm

import config


class DatabaseMiddleware(object):

    def process_resource(self, req, resp, resource, params):
        engine = sqlalchemy.create_engine(config.DATABASE)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        resource.db_session = Session()

    def process_response(self, req, resp, resource, req_succeeded):
        try:
            resource.db_session.commit()
        except:
            resource.db_session.rollback()
            raise
        finally:
            resource.db_session.close()
