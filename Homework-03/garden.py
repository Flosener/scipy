""" Class definition for a garden with plants. """

from citrus import Citrus

import random


class Garden:

    def __init__(self):
        """ Constructor for a garden. """
        
        self.plants = list()
        
    
    def __len__(self):
        """ Returns the number of plants currently in the garden. """
        
        return len(self.plants)
    
    
    def __str__(self):
        """ Returns the number of plants and unique species currently in the garden. """
        
        # append all species in the garden to support list
        species_list = list()
        for plant in self.plants:
            species_list.append(plant.species)
        
        return "<Garden with " + str(len(self)) + " plants and " + str(len(set(species_list))) + " species>"
    
    
    def plant(self, new_plant=None):
        """ Adds a new plant to this garden. """
        
        # add a new citrus plant with unspecified species if there is no specified plant
        if new_plant == None:
            self.plants.append(Citrus())
        else:
            # add specified plant
            self.plants.append(new_plant)
        
    def cross(self):
        """ Randomly crosses two citrus plants. The result is planted in the garden. """
        
        # if there are at least two plants in the garden, get two unique plant objects, cross and plant them
        if len(self) > 1:
            cross_plants = random.sample(self.plants, k=2)
            resulting_plant = cross_plants[0] + cross_plants[1]
            self.plant(resulting_plant)
            