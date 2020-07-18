from flask_restful import Resource, reqparse
from facade.planets import PlanetFacade


class Planets(Resource):
    @staticmethod
    def get():
        planet_list = []
        planets = PlanetFacade.get_all_planets()
        if planets:
            for planet in planets:
                planet_list.append(planet.parse_json())
            if planet_list:
                return planet_list
        return "Doesn't exist any planet! Please, create!"


class Planet(Resource):
    args = reqparse.RequestParser()
    args.add_argument(
        "name", type=str, required=True, help="Missing name")
    args.add_argument(
        "climate", type=str, required=True, help="Missing climate")
    args.add_argument(
        "terrain", type=str, required=True, help="Missing terrain")

    @staticmethod
    def get(planet_id):
        planet = PlanetFacade.find_planet_by_id(planet_id)
        if planet:
            return planet.parse_json(), 200

    @staticmethod
    def post(planet_id):
        data = Planet.args.parse_args()
        planet = PlanetFacade.save_planet(data, planet_id)
        if planet:
            return f"Planet {planet.name} was created successfully", 201
        return f"The {planet_id} was created before", 200

    def put(self, planet_id):
        data = self.args.parse_args()
        planet_updated = PlanetFacade.update_planet(data, planet_id)
        if planet_updated:
            return planet_updated.parse_json(), 200

    @staticmethod
    def delete(planet_id):
        planet_delete = PlanetFacade.delete_planet(planet_id)
        if planet_delete:
            return f"The {planet_delete} was deleted"
        return "Doesn't exist"


class GetPlanetsByName(Resource):

    @staticmethod
    def get(name):
        planet = PlanetFacade.find_planet_by_name(name)
        return planet.parse_json(), 200

