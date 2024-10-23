# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField


class WouldYouRather(Model):
    noun = StringField()
    noun2 = StringField()
    verb = StringField()
    timeschosen = IntegerField()
    happy = BooleanField()


    def json_response(self):
        return {
            'id': self.id,
            'scenario': self.noun + " " + self.verb + " " + self.noun2,
            'times chosen': self.timeschosen,
            'positive': self.happy
        }
    

    def change_verb(self, new_word):
        self.verb = new_word
        self.timeschosen = 0
        self.save()
          
    def change_noun(self, new_word):
        self.noun = new_word
        self.timeschosen = 0
        self.save()
 
    def change_noun2(self, new_word):
        self.noun2 = new_word
        self.timeschosen = 0
        self.save()

def json_options(self, id1, id2):
        
        return {
            'id': self.id,
            'scenario one': self.noun + " " + self.verb + " " + self.noun2,
            'OR':self,
            'scenario one': self.noun + " " + self.verb + " " + self.noun2,

        }