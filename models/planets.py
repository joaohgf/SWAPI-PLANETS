from database.db import database
import requests
import json


class PlanetModel(database.Model):
    __tablename__ = "planets"

    planet_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    climate = database.Column(database.String(80))
    terrain = database.Column(database.String(80))
    films_appear = database.Column(database.Integer)

    def __init__(self, name, climate, terrain):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.films_appear = PlanetModel.get_films(name)

    @staticmethod
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

    def parse_json(self):
        return {
            "planet_id": self.planet_id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "films_appear": self.films_appear
        }

    @classmethod
    def find_planet_by_id(cls, planet_id):
        if planet_id:
            try:
                planet = cls.query.filter_by(planet_id=planet_id).first()
            except Exception as error:
                return f"Error getting by id: {error}"
            if planet:
                return planet
            return None

    @classmethod
    def find_planet_by_name(cls, name):
        try:
            planet = cls.query.filter_by(name=name).first()
        except Exception as error:
            return f"Error getting by name: {error}"
        if planet:
            return planet
        return None

    @classmethod
    def get_all(cls):
        try:
            planets = cls.query.all()
        except Exception as error:
            return f"Error getting all {error}"
        if planets:
            return planets
        return None

    def save(self):
        try:
            database.session.add(self)
            database.session.commit()
        except Exception as error:
            return f"Error saving {error}"

    def update(self, name, climate, terrain):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.films_appear = PlanetModel.get_films(name)
        try:
            self.save()
        except Exception as error:
            return f"Error updating {error}"
        return self

    def delete(self):
        try:
            database.session.delete(self)
            database.session.commit()
        except Exception as error:
            return f"Error deleting{error}"
        return self.name
