# views.py

from banjo.urls import route_get, route_post
from .models import Rather
from settings import BASE_URL



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
    