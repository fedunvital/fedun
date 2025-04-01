from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age 

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"Ім'я: {self.__name}, Вік: {self.__age} років"

    def set_age(self, new_age):
        
        if new_age > 0:
            self.__age = new_age

class Sheep(Animal):
    def make_sound(self):
        return "Бе Ме Бе Ме!"

class Pig(Animal):
    def make_sound(self):
        return "Хрю-хрю!"

class Cow(Animal):
    def make_sound(self):
        return "Мууу!"

animals = [
    Sheep("Бараш", 4),
    Pig("Мейсо", 4),
    Cow("Мілка", 5)
]

for animal in animals:
    print(animal.get_info())
    print("Звук:", animal.make_sound())
    print("-")
