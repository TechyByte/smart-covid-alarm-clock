from uk_covid19 import Cov19API
import json
import pyttsx3

import app.utils

def covid_new_cases_uk():
    all_nations = ["areaType=nation"]

    cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }

    api = Cov19API(
    filters=all_nations,
    structure=cases_and_deaths,
    latest_by="newCasesByPublishDate"
    )

    data = api.get_json()
    #data = json.loads(data)
    total = 0
    for nation in data["data"]:
        total += nation["newCasesByPublishDate"]

    return total

def announcement():
    weather = app.utils.get_current_weather()
    speech = "Today the weather is " + weather[1] + " and the temperature is " + str(weather[0]) + " degrees " \
             "celsius. I've picked a headline to spark your curiosity: " + app.utils.get_current_news() + ". There have been " + \
             str(covid_new_cases_uk()) + "new coronavirus cases since yesterday."
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()

if __name__ == "__main__":
    announcement()