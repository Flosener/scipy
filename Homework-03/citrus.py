""" Class definition for a citrus plant. """

import random


class Citrus:

    def __init__(self, species=None, possible_species=("Pomelo", "Mandarin", "Citron")):
        """ Constructor for a citrus plant. """
        
        if species == None:
            self.species = random.choice(possible_species)
        else:
            self.species = species
        self.possible_species = possible_species
        
    
    def __str__(self):
        return "<Citrus of species " + str(self.species) + ">"
    
    
    def __add__(self, other):
        """ Method defining the genetic crossing of two citrus plants. """
        
        # if one of the objects is no citrus plant, raise TypeError
        if isinstance(self, Citrus) == False:
            raise TypeError(str(self) + " is no citrus plant!")
        if isinstance(other, Citrus) == False:
            raise TypeError(str(other) + " is no citrus plant!")
        
        # rules for genetic crossing of the plants
        if self.species == other.species:
            return Citrus(self.species)
        elif (self.species == "Pomelo" and other.species == "Mandarin") or (self.species == "Mandarin" and other.species == "Pomelo"):
            return Citrus(random.choice(["Sweet Orange", "Tangerine", "Satsuma", "Wildleaf Mandarin", "Bitter Orange"]))
        elif (self.species == "Pomelo" and other.species == "Sweet Orange") or (self.species == "Sweet Orange" and other.species == "Pomelo"):
            return Citrus("Grapefruit")
        elif (self.species == "Sweet Orange" and other.species == "Wildleaf Mandarin") or (self.species == "Wildleaf Mandarin" and other.species == "Sweet Orange"):
            return Citrus("Clementine")
        elif (self.species == "Citron" and other.species == "Bitter Orange") or (self.species == "Bitter Orange" and other.species == "Citron"):
            return Citrus("Lemon")
        else:
            return Citrus(random.choice([self.species, other.species]))
            

    def __radd__(self, other):
        raise TypeError(str(other) + " is no citrus plant!")