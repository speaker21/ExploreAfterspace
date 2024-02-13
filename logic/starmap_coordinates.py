import random

border = 10

def make_star_coordinates(map_width, map_height, stars_count):
    stars_list = []
    canvas_width = map_width - border
    canvas_height = map_height - border

    for _ in range(stars_count):
        x = random.randint(border, canvas_width)
        y = random.randint(border, canvas_height)
        stars_list.append((x, y))
    return stars_list