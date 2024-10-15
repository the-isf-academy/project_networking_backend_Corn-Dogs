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

    return {'fortune': new_scenario.json_response()}


@route_get(BASE_URL + 'all')
def all_scenarios(args):
    scenario_list = []

    for scenario in Rather.objects.all():
        scenario_list.append(scenario.json_response())

    return {'fortunes':scenario_list}