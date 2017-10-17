import boto3
import falcon

import middleware
import images
import users

boto3_session = boto3.Session(profile_name='find_it_dev')
rekognition_client = boto3_session.client('rekognition')

app = falcon.API(
    middleware=[
        middleware.DatabaseMiddleware(),
    ]
)
app.add_route('/image/recognize', images.Recognize(rekognition_client))
app.add_route('/user/create', users.Create())
