from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired


class AddAlarm(FlaskForm):
    trigger_datetime = DateField("Alarm time", validators=[DataRequired()], format="%d/%m/%Y, %H:%M")
    title = StringField("Title", validators=[DataRequired()])
    # content = StringField("Content")
    weather = BooleanField("Include weather briefing?")
    news = BooleanField("Include news briefing?")
    silent = BooleanField("Silent?")
    submit = SubmitField("Set alarm")
