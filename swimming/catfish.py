from datetime import date


class Catfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
