from Animal import Animal

class Lion(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, maneColor, prideSize):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__maneColor = maneColor
        self.__prideSize = prideSize


    def makeSound(self):
        return "Roar!"

    def getHabitat(self):
        return "Savanna"

    
class Elephant(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, tuskLength, weight):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__tuskLength = tuskLength
        self.__weight = weight


    def makeSound(self):
        return "Trumpet!"

    def getHabitat(self):
        return "Grassland"


class Monkey(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, tailLength, favoriteFood):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__tailLenght = tailLength
        self.__favoriteFood = favoriteFood


    def makeSound(self):
        return "Ooh ooh ah ah!"

    def getHabitat(self):
        return "Rainforest"