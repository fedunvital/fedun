from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError("Method fly() must be implemented")

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        raise NotImplementedError("Method swim() must be implemented")

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError("Method eat() must be implemented")

class Penguin(Swimmable, Eatable):
    def swim(self):
        print("Penguin is swimming")

    def eat(self):
        print("Penguin is eating")

class Sparrow(Flyable, Eatable):
    def fly(self):
        print("Sparrow is flying")

    def eat(self):
        print("Sparrow is eating")

# Використання
sparrow = Sparrow()
sparrow.fly()
sparrow.eat()
