from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    @abstractmethod
    def start_engine(self):
        pass

    def get_info(self):
        return f"Бренд: {self.__brand}, Модель: {self.__model}, Рік випуску: {self.__year}"

    def set_year(self, new_year):
        if new_year >= 1900:
            self.__year = new_year

class YamahaTT600(Vehicle):
    def start_engine(self):
        return "Yamaha TT600 запускає двигун: Брррррр-вжжжж!"

class MitsubishiOutlander2009(Vehicle):
    def start_engine(self):
        return "Mitsubishi Outlander 2009 запускає двигун: Врум-врум!"

vehicles = [
    YamahaTT600("Yamaha", "TT600", 2003),
    MitsubishiOutlander2009("Mitsubishi", "Outlander", 2009)
]

for vehicle in vehicles:
    print(vehicle.get_info())
    print("Звук двигуна:", vehicle.start_engine())
    print("-")
