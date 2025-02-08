# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")

    def eat(self):
        print(f"{self.name} is eating.")


# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} says chirp chirp!")


# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} says roar!")


# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} says hiss!")


# Демонстрация полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс Zoo, использующий композицию
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} to the zoo staff.")


# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")


# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


# Пример использования
if __name__ == "__main__":
    bird = Bird(name="Parrot", age=2, wing_span=25)
    mammal = Mammal(name="Lion", age=5, fur_color="Golden")
    reptile = Reptile(name="Snake", age=3, scale_type="Smooth")

    animals = [bird, mammal, reptile]
    animal_sound(animals)

    zoo = Zoo()
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    keeper = ZooKeeper(name="John")
    vet = Veterinarian(name="Dr. Smith")

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    keeper.feed_animal(mammal)
    vet.heal_animal(reptile)