import requests
import json
import pyyoutube as youtube
import os
import googleapiclient.discovery   
from flask_restful import Api, Resource
from dotenv import load_dotenv

class Food(Resource):
    def get(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = os.environ['YOUTUBE_API']
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.search().list(
        part="snippet",
        maxResults=50,
        order="relevance",
        q="food",
        regionCode="US",
        type="video",
        videoCategoryId="26"
        )
        response = request.execute()

        return response
