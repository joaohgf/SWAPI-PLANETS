from flask_restful import Resource, reqparse
from controller.planets import PlanetController
from flask_jwt_extended import jwt_required
import requests
import json


class Planets(Resource):
    @staticmethod
    def get():
        planet_list = []
        planets = PlanetController.get_all_planets()
        if planets:
            for planet in planets:
                planet_list.append(planet.parse_json())
            if planet_list:
                return {"Planets": planet_list}
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
        planet = PlanetController.find_planet_by_id(planet_id)
        if planet:
            return planet.parse_json(), 200

    @jwt_required
    def put(self, planet_id):
        data = self.args.parse_args()
        films_appear = get_films(data["name"])
        planet_updated = PlanetController.update_planet(
            data, planet_id, films_appear)
        if planet_updated:
            return planet_updated.parse_json(), 200

    @jwt_required
    def delete(self, planet_id):
        planet_delete = PlanetController.delete_planet(planet_id)
        if planet_delete:
            return f"The {planet_delete} was deleted", 200
        return "Doesn't exist"


class GetPlanetsByName(Resource):

    @staticmethod
    def get(name):
        planet = PlanetController.find_planet_by_name(name)
        return planet.parse_json(), 200


class CreatePlanet(Resource):

    @jwt_required
    def post(self):
        data = Planet.args.parse_args()
        films_appear = get_films(data["name"])
        planet = PlanetController.save_planet(data, films_appear)
        if planet:
            return f"Planet {data['name']} was created successfully", 201
        return f"The {data['name']} was created before"


def get_films(name):
    path = "https://swapi.dev/api/planets/?search=" + name
    try:
        req = requests.get(path)
    except Exception as error:
        return f"Error making request to S.W.A.P.I {error}"
    json_result = json.loads(req.text)
    if json_result["count"] > 0:
        return len(json_result["results"][0]["films"])
    return 0
