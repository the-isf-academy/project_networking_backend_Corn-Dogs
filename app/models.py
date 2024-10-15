# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField


class Rather(Model):
    noun = StringField()
    noun2 = StringField()
    verb = StringField()
    timechosen = IntegerField()
    happy = BooleanField()


    def json_response(self):
        
        return {
            'id': self.id,
            'scenario': self.noun + + self.verb + self.noun2,
            'times chosen': self.timechosen,
            'positive': self.happy
        }