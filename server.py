import boto3
import falcon

import images

boto3_session = boto3.Session(profile_name='find_it_dev')
rekognition_client = boto3_session.client('rekognition')

app = falcon.API()
app.add_route('/image/recognize', images.Recognize(rekognition_client))
