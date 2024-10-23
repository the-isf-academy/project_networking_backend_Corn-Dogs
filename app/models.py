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
            'positive': self.happy,
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

    def play_scenarios(self, id1, id2):
        scenario1 = WouldYouRather.objects.get(id=id1)      #defines scenario 1 and 2 as different IDs and words, which allows it to not return the same thing twice
        scenario2 = WouldYouRather.objects.get(id=id2)                               
        return {
            'Would You Rather': 
            
            f"{scenario1.noun} {scenario1.verb} {scenario1.noun2} OR {scenario2.noun} {scenario2.verb} {scenario2.noun2}"
        }
    
    def chosen_scenario(self, id1, id2):
        scenario1 = WouldYouRather.objects.get(id=id1)
        scenario2 = WouldYouRather.objects.get(id=id2) 
        return {
            'Would You Rather':
            f"{scenario1.noun} {scenario1.verb} {scenario1.noun2} OR {scenario2.noun} {scenario2.verb} {scenario2.noun2}"
            f"{scenario1.timeschosen}/{scenario2.timeschosen}"
        }

    def increase(self):
        self.timeschosen += 1
        self.save()