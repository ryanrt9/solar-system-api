from unicodedata import name
from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count

