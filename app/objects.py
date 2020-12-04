import datetime as dt
import hashlib
from urllib.parse import quote
from random import randrange


class Alarm:
    def __init__(self, time: str = "15/12/2020 09:00", silent: bool = True,
                 title: str = "Sample Title", content: str = "Sample Content", news: bool = False,
                 weather: bool = False, sched_obj=None):
        self.trigger_time = str(time)[:16]
        self.dt = dt.datetime.strptime(str(self.trigger_time), "%d/%m/%Y %H:%M")
        self.silent = silent
        self.title = title
        self.title_html = hashlib.sha256((self.title + str(randrange(0, 1010))).encode()).hexdigest()
        self.content = content
        self.news = news
        self.weather = weather
        self.sched_obj = sched_obj

