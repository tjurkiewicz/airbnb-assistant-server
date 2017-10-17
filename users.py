import falcon

import messages.findit_pb2
import models
import proto
import resources


class Create(resources.DatabaseResource):

    proto_request_class = messages.findit_pb2.CreateUserRequest

    @falcon.before(proto.parse_proto_from_request)
    def on_post(self, req, resp):
        if req.proto_request.name:
            user_instance = models.User(name=req.proto_request.name)
            self.db_session.add(user_instance)
            self.db_session.commit()
        else:
            resp.status = falcon.HTTP_BAD_REQUEST