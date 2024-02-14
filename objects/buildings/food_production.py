class FoodProduction:
    def __init__(self, size) -> None:
        self.food_production = 10000
        self.name = 'FoodProduction'
        # TODO COST
        self.size = size

    def build_new(self, planet_info_frame):
        self.size+=1
        planet_info_frame.update_build_production()