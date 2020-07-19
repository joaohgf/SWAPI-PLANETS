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
        planet = cls.find_planet_by_name(str(data["name"]))
        if planet:
            return planet.name
        planet_object = PlanetModel(films_appear, **data)
        planet_saved = PlanetModel.save(planet_object)
        if planet_saved:
            return planet_saved
        return None

    @classmethod
    def update_planet(cls, data, planet_id, films_appear):
        planet_result = cls.find_planet_by_id(planet_id)
        if planet_result:
            planet_updated = planet_result.update(**data)
            return planet_updated
        cls.save_planet(data, films_appear)

    @classmethod
    def delete_planet(cls, planet_id):
        planet_result = cls.find_planet_by_id(planet_id)
        if planet_result:
            return planet_result.delete()






