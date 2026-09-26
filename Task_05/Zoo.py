class Zoo:
    def __init__(self, zooName):
        self.__zooName = zooName
        self.__animals = []
        self.__zookeepers = []


    def addZookeepers(self, keeper):
        self.__zookeepers.append(keeper)

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def removeAnimal(self, animalId):
        self.__animals = [animal for animal in self.__animals if animal.animalId.lower() != animalId.lower()]

        for zookeeper in self.__zookeepers:
            zookeeper.removeAnimal(animalId)

    def assignAnimalToKeeper(self, animal, keeper):
        keeper.addAnimal(animal)

    def getAnimalsByHabitat(self, habitat):
        animals = []
        for animal in self.__animals:
            if animal.getHabitat().lower() == habitat.lower():
                animals.append(animal)

        return animals

    def getAnimalsBySpecies(self, species):
        animals = []
        for animal in self.__animals:
            if animal.species.lower() == species.lower():
                animals.append(animal)

        return animals

    def calculateTotalWeeklyCost(self):
        cost = 0
        for animal in self.__animals:
            cost += animal.calculateWeeklyCost()

        return cost


    def displayAllAnimals(self):
        for animal in self.__animals:
            print(animal.getAnimalInfo())

    def __countHabitatsHelper(self):
        habitats =[]
        for animal in self.__animals:
            habitat = animal.getHabitat().capitalize()
            if habitat not in habitats:
                habitats.append(habitat.capitalize())

        return habitats

    def __averageAnimalAgeHelper(self):
        sum = 0
        for animal in self.__animals:
           sum += animal.age 

        average = sum / len(self.__animals)
        return average

    def getZooStatistics(self):
        text_title = f"=== {self.__zooName.title()} Statistics ===\n"
        total_animals_text = f"Total Animals: {len(self.__animals)}\n"
        total_zookeeper_text = f"Total Zookeepers: {len(self.__zookeepers)}\n"
        habitats_represented_text = f"Habitats Represented: {len(self.__countHabitatsHelper())}\n"
        total_weekly_maintenance = f"Total Weekly Maintenance: ${self.calculateTotalWeeklyCost():0.2f}\n"
        average_animal_age_text = f"Average Animal Age: {self.__averageAnimalAgeHelper()} years\n"

        text = text_title + total_animals_text + total_zookeeper_text + habitats_represented_text +total_weekly_maintenance + average_animal_age_text
        return text

