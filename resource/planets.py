from flask_restful import Resource, reqparse
from facade.planets import PlanetFacade


class Planets(Resource):
    def get(self):
        planet_list = []
        planets = PlanetFacade.get_all_planets()
        for planet in planets:
            planet_list.append(planet.parse_json())
        return planet_list


class Planet(Resource):

    args = reqparse.RequestParser()
    args.add_argument("name")
    args.add_argument("climate")
    args.add_argument("terrain")

    def get(self, planet_id):
        planet = PlanetFacade.find_planet_by_id(planet_id)
        if planet:
            return planet.parse_json(), 200
        else:
            return f"Not found", 404

    def post(self, planet_id):
        data = Planet.args.parse_args()
        planet = PlanetFacade.save_planet(data, planet_id)
        if planet:
            return f"Planet {planet_id} was created successfully", 201
        return f"Error: Planet {planet_id} exists."

    def put(self, planet_id):
        data = self.args.parse_args()
        planet_updated = PlanetFacade.update_planet(data, planet_id)
        if planet_updated:
            return planet_updated.parse_json(), 200

    def delete(self, planet_id):
        planet_delete = PlanetFacade.delete_planet(planet_id)
        if planet_delete:
            return "Deleted"


class FindByName(Resource):

    def get(self, name):
        planet = PlanetFacade.find_planet_by_name(name)
        return planet.parse_json(), 200
