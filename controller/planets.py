from models.planets import PlanetModel


class PlanetController:
    def __init__(self):
        self.planet_controller = PlanetController()

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
    def save_planet(cls, data, films_appear):
        planet = PlanetModel.find_planet_by_name(str(data["name"]))
        if planet:
            return None
        planet_object = PlanetModel(films_appear, **data)
        planet_saved = PlanetModel.save(planet_object)
        if planet_saved:
            return planet_saved
        return None

    @classmethod
    def update_planet(cls, data, planet_id, films_appear):
        planet_result = PlanetModel.find_planet_by_id(planet_id)
        if planet_result:
            data["films_appear"] = films_appear
            planet_updated = planet_result.update(**data)
            return planet_updated

    @classmethod
    def delete_planet(cls, planet_id):
        planet_result = PlanetModel.find_planet_by_id(planet_id)
        if planet_result:
            return planet_result.delete()






