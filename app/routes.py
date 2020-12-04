from flask import render_template, redirect, request
import logging
import app.objects as objects
from app import app
from app.forms import AddAlarm
from urllib.parse import quote
import sched
import time
from app.announcement import announcement
from app.utils import get_current_weather, get_current_news

alarms = [objects.Alarm()]
s = sched.scheduler(time.time, time.sleep)


@app.route('/delete_alarm', methods=["GET", "POST"])
def delete_alarm():
    try:
        alarm_id = request.args.get("id")
    except AttributeError:
        logging.error("No alarm deletion id provided")
        return "Failure"

    try:
        logging.debug("Request received to delete alarm " + alarm_id)
    except TypeError:
        logging.debug("Invalid alarm deletion id provided")
        return "Invalid value provided"

    logging.debug(alarm_id)
    global alarms

    try:
        for alarm in alarms:
            if quote(alarm.title_html) == alarm_id:
                logging.debug("Alarm matched. Attempting deletion")
                alarms.remove(alarm)
                return "Success"
    except:
        logging.debug("Error removing alarm. Failing quietly...")
        return "Failure"
    logging.debug("No changes made to alarms.")
    return "No change"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global alarms
    global s
    notifications = []
    alerts = []
    logging.debug("Page requested..")
    form = AddAlarm()

    if form.title.data is not None:
        alarms.append(objects.Alarm(form.trigger_datetime.raw_data[0], form.silent.data, form.title.data, "Content", form.news.data, form.weather.data))
        logging.debug("Scheduling announcement")
        s.enter(10, 1, announcement)
        logging.debug("Queued")
        s.run(blocking=False)
        logging.debug("Alarm created: " + form.title.data)
        return redirect("/")

    for alarm in alarms:
        if alarm.silent:
            notifications.append(alarm)
        else:
            alerts.append(alarm)

    weather = get_current_weather(app.config["CURRENT_CITY"])
    return render_template('index.html', form=form, title=get_current_news(), alarms=alerts, notifications=notifications, icon_url=weather[2], temperature=weather[0], weather=weather[1])
