from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, animalId, name, species, age, healthStatus, dailyFoodCost):
        self.__animalId = animalId
        self.__name = name
        self.__species = species
        self.__age = age 
        self.__healthStatus = healthStatus
        self.__dailyFoodCost = dailyFoodCost


    @property
    def species(self):
        return self.__species

    @property
    def animalId(self):
        return self.__animalId

    @property
    def age(self):
        return self.__age

    @property
    def healthStatus(self):
        return self.__healthStatus

    @property
    def name (self):
        return self.__name

    @abstractmethod
    def makeSound(self):
        pass

    @abstractmethod
    def getHabitat(self):
        pass

    def getAnimalInfo(self):
        text = f"{self.__animalId} - {self.__name} ({self.__species}) - Age: {self.__age} - Habitat: {self.getHabitat()}"
        return text
        
    def calculateWeeklyCost(self):
        return 7*self.__dailyFoodCost
