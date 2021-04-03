from flask import Flask
from flask_restful import Api, Resource
import requests
import json
import pyyoutube as youtube
import os
import googleapiclient.discovery    

app = Flask(__name__)
api = Api(app)

class Games(Resource):
    def get(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyAHo_GOTbmwwG1UlLd0JLZo4UAhcI_yWgM"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.search().list(
        part="snippet",
        maxResults=50,
        order="viewCount",
        regionCode="US",
        type="video",
        videoCategoryId="20"
        )
        response = request.execute()

        return response

class Food(Resource):
    def get(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyAHo_GOTbmwwG1UlLd0JLZo4UAhcI_yWgM"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.search().list(
        part="snippet",
        maxResults=25,
        order="relevance",
        q="food",
        regionCode="US",
        type="video",
        videoCategoryId="26"
        )
        response = request.execute()

        return response

class Comedy(Resource):
    def get(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyAHo_GOTbmwwG1UlLd0JLZo4UAhcI_yWgM"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.search().list(
        part="snippet",
        maxResults=50,
        order="viewCount",
        regionCode="US",
        type="video",
        videoCategoryId="23"
        )
        response = request.execute()

        return response


api.add_resource(Games, '/gaming')
api.add_resource(Food, '/food')
api.add_resource(Comedy, '/comedy')

if __name__ == '__main__':
    app.run(debug = True)

