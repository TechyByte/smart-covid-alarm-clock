import json
import logging

import requests

from app import app


def get_current_weather(location: str = app.config["CURRENT_CITY"]) -> [float, str, str]:
    """
    Gets required weather information for a given location
    :param location: Location to get weather at
    :return: [temperature, conditions as text, url for icon display]
    """
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url=api_url, params=dict(appid=app.config["OPENWEATHER_API_KEY"], q=location, units="metric"))
    jr = json.loads(r.content)
    icon_url = "https://openweathermap.org/img/wn/" + jr["weather"][0]["icon"] + "@4x.png"
    temp = jr["main"]["temp"]
    description = jr["weather"][0]["description"]
    return [temp, description, icon_url]


def get_current_news() -> str:
    """
    Gets a UK headline
    :return: A headline to display for today.
    """
    api_url = 'http://newsapi.org/v2/top-headlines'
    logging.debug("Making request to: " + api_url + "  Country: gb")
    r = requests.get(url=api_url, params=dict(apiKey=app.config["NEWS_API_KEY"], country="gb"))
    jr = json.loads(r.content)
    logging.debug(r.content)

    # Shorten headline to 50 characters and also handle the error that would arise from a failed attempt to get news
    try:
        return jr["articles"][0]["title"] + ("..." if len(jr["articles"][0]["title"]) < 50 else "")
    except IndexError:
        return "There's currently no news for you!"