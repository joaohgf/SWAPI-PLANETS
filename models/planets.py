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

    def __init__(self, planet_id, name, climate, terrain, films_appear):
        self.planet_id = planet_id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.films_appear = films_appear

    @classmethod
    def get_films(cls, name):
        path = "https://swapi.dev/api/planets/?search=" + name
        req = requests.get(path)
        json_result = json.loads(req)


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
            planet = cls.query.filter_by(planet_id=planet_id).first()
            if planet:
                return planet
            return None

    @classmethod
    def find_planet_by_name(cls, name):
        planet = cls.query.filter_by(name=name).first()
        if planet:
            return planet
        return None

    @classmethod
    def get_all(cls):
        planets = cls.query.all()
        if planets:
            return planets
        return None

    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, name, climate, terrain, films_appear):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.films_appear = super(PlanetModel.get_films(name))
        self.save()
        return self

    def delete(self):
        database.session.delete(self)
        database.session.commit()
        return self