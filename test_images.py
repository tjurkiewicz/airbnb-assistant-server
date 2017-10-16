import json
import os

import botocore.client
import botocore.stub
import botocore.session
import falcon
import pytest

import messages.findit_pb2
import images


@pytest.fixture
def images_recognize(app, default_route, rekognition_client):
    handler = images.Recognize(rekognition_client)
    app.add_route(default_route, handler)


@pytest.fixture(scope='session')
def recognition_payload():
    with open(os.path.join('test_data', 'recognition_payload.pb'), 'rb') as f:
        return f.read()


@pytest.fixture
def rekognition_client():
    client = botocore.session.get_session().create_client('rekognition')
    stub = botocore.stub.Stubber(client)

    with open(os.path.join('test_data', 'aws_rekognition_ok_response.json'), 'rb') as f:
        stub.add_response('detect_labels', json.load(f))

    stub.activate()
    return client


def test_recognition(client, default_route, images_recognize, recognition_payload):
    resp = client.post(default_route, data=recognition_payload)

    assert resp.status == falcon.HTTP_OK
    proto_response = messages.findit_pb2.RecognitionResponse()
    proto_response.ParseFromString(resp.body)
    assert len(proto_response.recognition_labels) == 4
