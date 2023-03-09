from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class RatingForm(FlaskForm):
    site = StringField('site')
    submit = SubmitField('Проверить')
