from flask import Flask
from comdey import Comedy
from food import Food
from games import Games
from flask_restful import Api
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)
api = Api(app)

api.add_resource(Games, '/gaming')
api.add_resource(Food, '/food')
api.add_resource(Comedy, '/comedy')

if __name__ == '__main__':
    if os.environ['ENV'] == 'dev':
        app.run(debug = True)
    else:
        app.run()

