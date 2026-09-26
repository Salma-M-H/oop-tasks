class Zookeeper:
    def __init__(self, employeeId, name, specialization):
        self.__employeeId = employeeId
        self.__name = name
        self.__specialization = specialization
        self.__assignedAnimals = []

    @property
    def assignedAnimals(self):
        return self.__assignedAnimals

    @property
    def name(self):
        return self.__name

    def feedAnimal(self, animal):
        print(f"{self.__name} fed {animal.name} ({animal.species})")
    
    def checkHealth(self, animal):
        print(f"{self.__name} checked health of {animal.name} ({animal.species}) - Status: {animal.healthStatus}")
        

    def getWorkload(self):
        return len(self.__assignedAnimals)

    def addAnimal(self, animal):
        self.__assignedAnimals.append(animal)

    def removeAnimal(self, animalId):
        for animal in self.__assignedAnimals:
            if animal.animalId.lower() == animalId.lower():
                self.__assignedAnimals.remove(animal)
                break