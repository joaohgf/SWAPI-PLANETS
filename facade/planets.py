from models.planets import PlanetModel


class PlanetFacade:
    def __init__(self):
        self.planet_facade = PlanetFacade()

    @classmethod
    def find_planet_by_id(cls, planet_id):
        planet_obj = PlanetModel.find_planet_by_id(planet_id)
        if planet_obj:
            return planet_obj

    @classmethod
    def find_planet_by_name(cls, name):
        planet_obj = PlanetModel.find_planet_by_name(name)
        if planet_obj:
            return planet_obj

    @classmethod
    def get_all_planets(cls):
        planets = PlanetModel.get_all()
        if planets:
            return planets
        return None

    @classmethod
    def save_planet(cls, data, planet_id, films_appear):
        if PlanetFacade.find_planet_by_id(planet_id):
            return None
        planet_saved = PlanetModel(planet_id, **data)
        planet_saved.save()
        if planet_saved:
            return planet_saved
        return None

    @classmethod
    def update_planet(cls, data, planet_id):
        planet_result = PlanetFacade.find_planet_by_id(planet_id)
        if planet_result:
            planet_updated = planet_result.update(**data)
            return planet_updated

    @classmethod
    def delete_planet(cls, planet_id):
        planet_result = PlanetFacade.find_planet_by_id(planet_id)
        if planet_result:
            return planet_result.delete()






