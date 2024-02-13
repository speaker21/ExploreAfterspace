import json
from objects.celestials.basic_star import Star

def celestials_init(game_state):
    with open('data/stars.json', 'r', encoding='utf-8') as stars_json:
        star_list = json.load(stars_json)
    for star in star_list:
        star_object = Star(star, game_state)
        game_state.stars_list.append(star_object)