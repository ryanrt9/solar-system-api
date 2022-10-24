from unicodedata import name
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count

planets = [Planet(1, "Mercury", "Closest to the sun", 0), 
Planet(2, "Venus", "Planet of love", 0),
Planet(3, "Earth", "Third rock from the sun", 1),
Planet(4, "Mars", "Red planet", 2),
Planet(5, "Jupiter", "The Gas Giant", 57),
Planet(6, "Saturn", "Astroid Rings", 63),
Planet(7, "Uranus", "empty", 27),
Planet(1, "Neptune", "Can't see with naked eye", 14) 
]     

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])

def get_all_planets():
    planets_response = []
    
    for planet in planets:
        planets_response.append({"id":planet.id, 
        "name": planet.name, 
        "description": planet.description,
        "moon_count": planet.moon_count})

    return jsonify(planets_response)