
import falcon

import messages.findit_pb2
import proto


class Recognize(object):

    proto_request_class = messages.findit_pb2.RecognitionRequest

    def __init__(self, rekognition_client):
        self._rekognition_client = rekognition_client


    @falcon.before(proto.parse_proto_from_request)
    @falcon.after(proto.serialize_proto_response)
    def on_post(self, req, resp):
        rekognition_response = self._rekognition_client.detect_labels(
            Image={
                'Bytes': req.proto_request.payload,
            },
        )

        proto_response = messages.findit_pb2.RecognitionResponse()
        for l in rekognition_response.get('Labels', {}):
            label = proto_response.recognition_labels.add()
            label.name = l['Name']
            label.confidence = l['Confidence']

        resp.proto_response = proto_response
