from Animal import Animal

class Crocodile(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, jawStrength, weight):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__jawStrength = jawStrength
        self.__weight = weight


    def makeSound(self):
        return "Growl!"

    def getHabitat(self):
        return "Swamp"


class Snake(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, isVenomous, length):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__isVenomous = isVenomous
        self.__length = length


    def makeSound(self):
        return "Hiss!"

    def getHabitat(self):
        return "Desert"