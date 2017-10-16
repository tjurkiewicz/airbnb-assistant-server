
import logging

import messages.findit_pb2

Logger = logging.getLogger(__name__)


class Recognize(object):

    def __init__(self, rekognition_client):
        self._rekognition_client = rekognition_client

    def on_post(self, req, resp):

        proto_request = messages.findit_pb2.RecognitionRequest()
        proto_request.ParseFromString(req.stream.read())

        rekognition_response = self._rekognition_client.detect_labels(
            Image={
                'Bytes': proto_request.payload,
            },
        )

        proto = messages.findit_pb2.RecognitionResponse()

        for l in rekognition_response.get('Labels', {}):
            label = proto.recognition_labels.add()
            label.name = l['Name']
            label.confidence = l['Confidence']

        resp.content_type = 'application/octet-stream'
        resp.data = proto.SerializeToString()

