
import models
import resources


class Create(resources.DatabaseResource):

    def on_post(self, req, resp):
        user_instance = models.User(name='name')
        self.db_session.add(user_instance)
        self.db_session.commit()
