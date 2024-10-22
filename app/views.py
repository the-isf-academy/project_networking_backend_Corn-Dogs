# views.py

from banjo.urls import route_get, route_post
from .models import Rather
from settings import BASE_URL
from random import *
from num2words import num2words         #pip install num2words in terminal


@route_post(BASE_URL + 'new', args={'noun':str, 'verb':str, 'noun2':str, 'happy': bool})
def new_scenario(args):
    new_scenario = Rather(
        noun = args['noun'],
        verb = args['verb'],
        noun2 = args['noun2'],
        happy = args['happy'],
        timechosen = 0
    )

    new_scenario.save()

    return {'riddle': new_scenario.json_response()}


@route_get(BASE_URL + 'all')
def all_scenarios(args):
    scenario_list = []

    for scenario in Rather.objects.all():
        scenario_list.append(scenario.json_response())

    return {'riddles':scenario_list}



@route_post(BASE_URL +'change', args={'id':int, 'wordclass':str, 'new_word':str})
def change_scenario(args):
    if Rather.objects.filter(id=args['id']).exists():

        one_rather = Rather.objects.get(id=args['id'])

        if args['wordclass'] == 'noun':
            one_rather.change_noun(args['new_word'])

        elif args['wordclass'] == 'verb':
            one_rather.change_verb(args['new_word'])

        elif args['wordclass'] == 'noun2':
            one_rather.change_noun2(args['new_word'])

        else:
            return {"changing scenario":"no word class exists. please enter either 'noun', 'verb', or 'noun2'."}
    
        return {'scenario': one_rather.json_response()}
    else:
        return {'erorr':'no fortune exists'}
    

@route_get(BASE_URL +'option')    ##where the user gets given two random scenarios/options
def choose_scenario(args):
    good_list = []
    bad_list = []
    scenario_matches =[] 

    for scenario in Rather.objects.all():
        if scenario.happy == True:       #sorts them into good and bad (in order to be fair)
            good_list.append(scenario.json_response())
        else:
            bad_list.append(scenario.json_response)

    mood = random.choice(good_list, bad_list)   #chooses randomly between good or bad

    scenario1 = random.choice(mood)(id=args['id'])        #these four lines chooses two random scenarios with the same mood 
    scenario1 = scenario1.id                              #and stores only their id
    scenario2 = random.choice(mood)
    scenario2 = scenario2.id

    for i in range():  
        kevin = []                                                       #defns it as a list         
        kevin.append(scenario1)                                          #adds scen. 1 and 2 to the list
        kevin.append(scenario2)
        kevin = num2words(len(scenario_matches)+1) 
        scenario_matches.append(num2words(len(scenario_matches)+1) )       #adds them to matches





    #randomly picks two of the same positivity
    #json response of the two scenarios
    #then names them something
    #adds the name to scneario_matches


@route_post(BASE_URL +'choose', args={'id':int, 'wordclass':str, 'new_word':str})
def choose_scenario(args):
    
    #gets the most recent input as your matched scenarios
    #

    #option - get two random options
    #delete
    #choice - make a choice between the two options (link into option somehow?) 