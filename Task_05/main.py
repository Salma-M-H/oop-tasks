from Animal import Animal
from Zoo import Zoo
from Zookeeper import Zookeeper
from Mammal import Lion, Elephant, Monkey
from Birds import Parrot, Eagle
from Rebtile import Snake, Crocodile

# create the zoo
zoo = Zoo("Safari World")

# create animals
lion = Lion("A001", "Simba", "African Lion", 5, "Healthy", 50.00, "Golden", 3)
elephant = Elephant("A002", "Dumbo", "African Elephant", 15, "Healthy", 80.00, 2.5, 5000)
parrot = Parrot("A003", "Polly", "Macaw", 8, "Healthy", 10.00, True)
snake = Snake("A004", "Kaa", "Python", 10, "Healthy", 15.00, True, 4.5)
eagle = Eagle("A005", "Freedom", "Bald Eagle", 6, "Healthy", 20.00, 2.3, 320)

parrot.addVocabulary("Hello")
parrot.addVocabulary("Goodbye")
parrot.addVocabulary("Pretty bird")

# Check Sound
# print(lion.makeSound())
# print(elephant.makeSound())
# print(parrot.makeSound())
# print(snake.makeSound())
# print(eagle.makeSound())

# Check Habitat
# print(lion.getHabitat())
# print(elephant.getHabitat())
# print(parrot.getHabitat())
# print(snake.getHabitat())
# print(eagle.getHabitat())

# Check Animal Info
# print(lion.getAnimalInfo())
# print(elephant.getAnimalInfo())
# print(parrot.getAnimalInfo())
# print(snake.getAnimalInfo())
# print(eagle.getAnimalInfo())

# Check Weekly Cost
print(lion.calculateWeeklyCost())
print(elephant.calculateWeeklyCost())
print(parrot.calculateWeeklyCost())
print(snake.calculateWeeklyCost())
print(eagle.calculateWeeklyCost())

# Parrot
# print(parrot.speak())


# Add Animals to Zoo
zoo.addAnimal(lion)
zoo.addAnimal(elephant)
zoo.addAnimal(parrot)
zoo.addAnimal(snake)
zoo.addAnimal(eagle)

# remove animal
# zoo.displayAllAnimals()
# zoo.removeAnimal(lion.animalId)
# zoo.displayAllAnimals()

# Animals By Habitat
# print(zoo.getAnimalsByHabitat('mountains'))

# Animals By Species
# print(zoo.getAnimalsBySpecies('African Elephant'))

# Zoo Statistics
# print(zoo.getZooStatistics())


# Create Zookeeper
keeper1 = Zookeeper("K001", "John Smith", "Mammals")
keeper2 = Zookeeper("K002", "Jane Doe", "Birds and Reptiles")

# Add keepers to zoo
zoo.addZookeepers(keeper1)
zoo.addZookeepers(keeper2)

# Assigned Animals to Keepers
zoo.assignAnimalToKeeper(lion, keeper1)
zoo.assignAnimalToKeeper(elephant, keeper1)
zoo.assignAnimalToKeeper(parrot, keeper2)
zoo.assignAnimalToKeeper(snake, keeper2)
zoo.assignAnimalToKeeper(eagle, keeper2)

# Check Health
# print(keeper1.checkHealth(lion))
# print(keeper2.checkHealth(snake))

# Work Load
# print(keeper1.getWorkLoad())

# print(keeper1.assignedAnimals)
# zoo.displayAllAnimals()
# zoo.removeAnimal('A001')
# print(keeper1.assignedAnimals)

print(zoo.getZooStatistics())

print("\n=== Zookeeper Activities ===")
keeper1.feedAnimal(lion)
keeper1.checkHealth(elephant)
print(f"{keeper1.name}'s workload:{keeper1.getWorkload()} animals")