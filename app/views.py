# views.py

from banjo.urls import route_get, route_post
from .models import WouldYouRather
from settings import BASE_URL
from random import *


routeoptions = ['new', 'all', 'one', 'change', 'option', 'delete', 'help']
matching = [] 


@route_post(BASE_URL + 'new', args={'noun':str, 'verb':str, 'noun2':str, 'happy': bool})
def new_scenario(args):

    new_scenario = WouldYouRather(
        noun = args['noun'],
        verb = args['verb'],
        noun2 = args['noun2'],
        happy = args['happy'],
        timeschosen = 0
    )
    if args['happy'] not in args:
        return {"errors": { "happy":  "This field is required."}}       #makes sure happy is included (because all booleans default to False, so if it's not given, it'll automatically show up as a negative scenario and cause no automatic errors like the others.)
    
    new_scenario.save()

    return {'scenario': new_scenario.json_response()}



@route_get(BASE_URL + 'all')
def all_scenarios(args):
    scenarios_list = []

    for scenario in WouldYouRather.objects.all():
        if (scenario.noun == '' or scenario.noun.isspace() or          #these two chunks of code make sure it doesnt return something empty 
        scenario.verb == '' or scenario.verb.isspace() or 
        scenario.noun2 == '' or scenario.noun2.isspace()):
            scenario.delete()
        else:
            scenarios_list.append(scenario.json_response())

    return {'scenarios': scenarios_list}



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
    happylist = ['good', 'bad']

    for scenario in WouldYouRather.objects.all():     #sorts them the scenarios into good and bad
        if scenario.happy == True:     
            good_list.append(scenario)
        else:
            bad_list.append(scenario)

    mood = choice(happylist)   #chooses randomly between a good or bad mood to give
    if mood == 'good':
        scenario_list = good_list
    else:
        scenario_list = bad_list
        
    scenario1 = choice(scenario_list)       #chooses two scenarios from the same mood list
    scenario2 = choice(scenario_list)

    while scenario1.id == scenario2.id:      #reselects scenario 2 until they're different
        scenario2 = choice(scenario_list)

    while (scenario1.noun == '' or scenario1.noun.isspace() or          #these two chunks of code make sure it doesnt return something empty 
        scenario1.verb == '' or scenario1.verb.isspace() or 
        scenario1.noun2 == '' or scenario1.noun2.isspace()):            #cool function that "eturns True if all the characters in a string are whitespaces" (w3schools.com)
        scenario1 = choice(scenario_list)
        while scenario1.id == scenario2.id:                             #and at the same time makes sure it doesn't select the same scenarios again
            scenario2 = choice(scenario_list)

    while (scenario2.noun == '' or scenario2.noun.isspace() or 
        scenario2.verb == '' or scenario2.verb.isspace() or 
        scenario2.noun2 == '' or scenario2.noun2.isspace()):
        scenario2 = choice(scenario_list)
        while scenario1.id == scenario2.id:
            scenario2 = choice(scenario_list)
    
    matching.clear()                                                                     #clears the previous match's imformation
    oneresp = scenario1.json_response()
    tworesp = scenario2.json_response()
    matching.append(oneresp)                                            #stores the current game for choosing (next step)
    matching.append(tworesp)
    return {'Game': scenario1.json_play(scenario1.id, scenario2.id)}                #returns your options






@route_post(BASE_URL + 'choose', args={'option': int})
def choose_scenario(args):
    scenario1 = WouldYouRather.objects.get(id=matching[0]['id'])
    scenario2= WouldYouRather.objects.get(id=matching[1]['id'])
    if args['option'] == 1:
        scenario1.increase()

    elif args['option'] == 2:
        scenario2.increase()
    else:
        return {'error': 'maximum comparison is 2 or invalid option'}
    return {'GAME': scenario1.json_chosen(scenario1.id, scenario2.id)}





@route_get(BASE_URL + 'help')           #if people want help knowing what methods are available, they can use /help
def help(args):
    formattedoptions = []
    i = 1
    for option in routeoptions:
        formattedoptions.append(f"{i}. {option}")
        i += 1
    formattedoptions.append("For more help, visit the README.md file.")
    return {'route options': formattedoptions}



@route_post(BASE_URL + 'delete', args={'id': int, 'password': str})
def delete_scenario(args):
    scenario_id_to_delete = args['id']
    
    # Check if the scenario exists
    scenario_to_delete = WouldYouRather.objects.filter(id=scenario_id_to_delete).first()

    if scenario_to_delete:
        # Check for the correct password
        if args['password'] == 'chromebook':                        #password for deletion to have some security so random people can't delete random scenarios
            # Store the ID for later use
            delete_scenario_id = scenario_to_delete.id
            scenario_to_delete.delete()

            return {'DELETING': scenario_to_delete.json_response()}

        else:
            return {'error': 'Authorization password incorrect.'}
    else:
        return {'error': 'No scenario exists with that ID.'}