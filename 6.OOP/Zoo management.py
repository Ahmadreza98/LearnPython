class Animal:
    zoo_name = "North ZOO"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.sound}")

    def info(self):
        return (f"Name: {self.name},\nSpecies: {self.species},\n"
                f"Age: {self.age},\nSound: {self.sound}")

    def __str__(self):
        return (f"The {self.name} is a animal, him species is "
                f"{self.species} and age, {self.age} year old. "
                f"The Lion's sound is '{self.sound}'.")


class Bird(Animal):
    wing_span = 12

    def __init__(self, name, species, age, sound):
        super().__init__(name, species, age, sound)

    def make_sound(self):
        return f"CHIK! CHIK!"


lion = Animal("Lion", "Mammal", 12, "AHHHHHH")

print(lion)
print(lion.zoo_name)
print(lion.info())
