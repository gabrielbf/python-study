class Dog:
    species = 'mammal'

    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    def eat(self):
        self.is_hungry = False


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    def eat(self):
        self.is_hungry = False


class Pets:
    def __init__(self, *args):
        self.pets = args

    def description(self):
        print("I have {} dogs.".format(len(self.pets)))
        hungry = False
        for pet in self.pets:
            if pet.is_hungry:
                hungry = True
            print("{} is {}.".format(pet.name, pet.age))
        print("And they're all {}s, of course.".format(self.pets[0].species))
        if hungry:
            print("My dogs are hungry.")
        else:
            print("My dogs are not hungry.")
