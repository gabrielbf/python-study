"""
Using the same Dog class, instantiate three new dogs, each with a different
age. Then write a function called, get_biggest_number(), that takes any
number of ages (*args) and returns the oldest one. Then output the age of
the oldest dog like so: The oldest dog is 7 years old.
"""


class Dog:

    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_dog_primeira_implementacao(*args):
    oldest = 0
    for age in args:
        if age > oldest:
            oldest = age
    return "The oldest dog is {} years old".format(oldest)


def oldest_dog(*args):
    return "The oldest dog is {} years old".format(max(args))


fofa = Dog("Fofa Dorotéia", 13)
avery = Dog("Avery", 3)
nicole = Dog("Nicole Cristine", 12)


if __name__ == "__main__":
    oldest_dog(fofa.age, avery.age, nicole.age)
