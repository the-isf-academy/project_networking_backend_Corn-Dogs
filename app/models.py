# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField


class Rather(Model):
    noun = StringField()
    adjective = StringField()
    verb = StringField()