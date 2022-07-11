from traits_people import PeopleTraits, somePeopleTraits


class Religion:
    def __init__(self, name, traits):
        self.name = name
        self.desirable : list[PeopleTraits] = traits[0]
        self.undesirable : list[PeopleTraits] = traits[1]
    
    def __str__(self):
        return f"Religion: {self.name}. Desirable Trairs: {self.desirable}, Undesirable Traits: {self.undesirable}"