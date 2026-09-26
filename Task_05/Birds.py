from Animal import Animal
import random

class Parrot(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, canTalk):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__canTalk = canTalk
        self.__vocabulary = []

    def addVocabulary(self, word):
        self.__vocabulary.append(word)
        
    def makeSound(self):
        return "Squawk!"

    def speak(self):
        return random.choice(self.__vocabulary)

    def getHabitat(self):
        return "Rainforest"

class Eagle(Animal):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost, wingspan, diveSpeed):
        super().__init__(animalId, name, species, age, healthStatus, dailyFoodCost)
        self.__wingspan = wingspan
        self.__diveSpeed = diveSpeed

    def makeSound(self):
        return "Screech!"

    def getHabitat(self):
        return "Mountains"