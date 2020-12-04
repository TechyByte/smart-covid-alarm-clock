import os
import json


class Config(object):
    with open('config.json') as json_file:
        data = json.load(json_file)
        OPENWEATHER_API_KEY = data["OPENWEATHER_API_KEY"]
        NEWS_API_KEY = data["NEWS_API_KEY"]
        SECRET_KEY = data["SECRET_KEY"]
        CURRENT_CITY = "Exeter, UK"