# views.py

from banjo.urls import route_get, route_post
from .models import WouldYouRather
from settings import BASE_URL
from random import *
from num2words import num2words         #pip install num2words in terminal


@route_post(BASE_URL + 'new', args={'noun':str, 'verb':str, 'noun2':str, 'happy': bool})
def new_scenario(args):
    new_scenario = WouldYouRather(
        noun = args['noun'],
        verb = args['verb'],
        noun2 = args['noun2'],
        happy = args['happy'],
        timeschosen = 0
    )

    new_scenario.save()

    return {'scenario': new_scenario.json_response()}


@route_get(BASE_URL + 'all')
def all_scenarios(args):
    scenario_list = []

    for scenario in WouldYouRather.objects.all():
        scenario_list.append(scenario.json_response())

    return {'riddles':scenario_list}

@route_get(BASE_URL + 'one', args={'id':int})
def all_scenarios(args):
    if WouldYouRather.objects.filter(id=args['id']).exists():
        one_scenario = WouldYouRather.objects.get(id=args['id'])
        return {'scenario': one_scenario.json_response()}
    else:
        return {'error':'no fortune exists'}



@route_post(BASE_URL +'change', args={'id':int, 'wordclass':str, 'new_word':str})
def change_scenario(args):
    if WouldYouRather.objects.filter(id=args['id']).exists():

        one_scenario = WouldYouRather.objects.get(id=args['id'])

        if args['wordclass'] == 'noun':
            one_scenario.change_noun(args['new_word'])

        elif args['wordclass'] == 'verb':
            one_scenario.change_verb(args['new_word'])

        elif args['wordclass'] == 'noun2':
            one_scenario.change_noun2(args['new_word'])

        else:
            return {"changing scenario":"no word class exists. please enter either 'noun', 'verb', or 'noun2'."}
    
        return {'scenario': one_scenario.json_response()}
    
    else:
        return {'error':'no fortune exists'}
    

@route_get(BASE_URL +'option')    ##where the user gets given two random scenarios/options
def choose_scenario(args):
    good_list = []
    bad_list = []
    lists = [good_list, bad_list]
    scenario_matches =[] 

    for scenario in WouldYouRather.objects.all():
        if scenario.happy == True:       #sorts them into good and bad (in order to be fair)
            good_list.append(scenario.json_response())
        else:
            bad_list.append(scenario.json_response)

    mood = random.choice(lists)   #chooses randomly between good or bad

    scenario1 = random.choice(mood)(id=args['id'])        #these four lines chooses two random scenarios with the same mood 
    scenario1 = scenario1.id                              #and stores only their id
    scenario2 = random.choice(mood)
    scenario2 = scenario2.id


    kevin = []                                                       #defns a list         
    kevin.append(scenario1)                                          #adds scen. 1 and 2 to the list
    kevin.append(scenario2)
    kevin = num2words(len(scenario_matches)+1)                       #new name
    scenario_matches.append(num2words(len(scenario_matches)+1) )       #adds them to matches
    return(scenario_matches)





    #randomly picks two of the same positivity
    #json response of the two scenarios
    #then names them something
    #adds the name to scneario_matches


@route_post(BASE_URL + 'delete', args={'id':int,'password':str})
def delete_scenario(args):
    if WouldYouRather.objects.filter(id=args['id']).exists():
        if args['password'] == 'Chromebook':
            return {'deleting scenario': delete_scenario.json_response()}
            WouldYouRather.objects.get(id=args['id']).delete()
        else:
            return {'error':'authrorization password incorect'}
    else:
        return {'error':'no fortune exists'}
    

#@route_post(BASE_URL +'choose', args={'id':int, 'wordclass':str, 'new_word':str})
#def choose_scenario(args):
    
    #gets the most recent input as your matched scenarios


    #option - get two random options
    #delete
    #choice - make a choice between the two options (link into option somehow?) 