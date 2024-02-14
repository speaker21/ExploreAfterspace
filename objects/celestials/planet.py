from objects.buildings.food_production import FoodProduction

class Planet:
    def __init__(self, planet):
        self.name = planet['name']
        if 'population' in planet:
            self.population = planet['population']
        else:
            self.population = None
        self.ore = planet['ore']
        self.gas = planet['gas']
        self.food = planet['food']
        self.buildings = []
        if 'buildings' in planet:
            for build in planet['buildings']:
                if build['name'] == 'food_production':
                    build_object = FoodProduction(build['size'])
                    self.production_building = build_object
                    self.buildings.append(build_object)
        else:
            self.production_building = FoodProduction(0)


    def calculate_state(self):
        self.food_production_and_consumption()
        self.calculate_population()

    def calculate_population(self):
        if self.food<0:
            self.population+=self.food
            self.food=0
        elif self.food>0:
            self.population=self.population+round((self.population/100)*10)

    def use_resources(self):
        # TODO
        self.ore-=10
        self.gas-=20

    def food_production_and_consumption(self):
        self.food += self.production_building.food_production*self.production_building.size
        self.food = self.food - round(self.population*0.7)