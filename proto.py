

def parse_proto_from_request(req, resp, resource, params):
    req.proto_request = resource.proto_request_class()
    req.proto_request.ParseFromString(req.stream.read())


def serialize_proto_response(req, resp, resource):
    resp.content_type = 'application/octet-stream'
    resp.data = resp.proto_response.SerializeToString()
