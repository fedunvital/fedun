class Equipment:
    def __init__(self):
        self._name = ""
        self._price = 0

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def show(self):
        print(f"{self.get_name()}: ${self.get_price()}")


class Engine(Equipment):
    def __init__(self):
        super().__init__()
        self.set_name("Engine")
        self.set_price(800)


class Body(Equipment):
    def __init__(self):
        super().__init__()
        self.set_name("Body")
        self.set_price(3000)


class Tools(Equipment):
    def __init__(self):
        super().__init__()
        self.set_name("Tools")
        self.set_price(4000)


class Composite(Equipment):
    def __init__(self):
        super().__init__()
        self._equipments = []

    def add(self, equipment):
        self._equipments.append(equipment)

    # Можна раскоментувати для видалення
    # def remove(self, equipment):
    #     self._equipments = [eq for eq in self._equipments if eq != equipment]

    def get_price(self):
        return sum(equipment.get_price() for equipment in self._equipments)

    def show(self):
        print(f"{self.get_name()}: ${self.get_price()}")
        for equipment in self._equipments:
            equipment.show()


class Car(Composite):
    def __init__(self):
        super().__init__()
        self.set_name("Audi")


# Використання
engine = Engine()
body = Body()
tools = Tools()

car = Car()
car.add(engine)
car.add(body)
car.add(tools)
car.add(tools)  # двічі додаємо tools

car.show()

# Можна додати:
# print(f"Загальна ціна: ${car.get_price()}")
# car.remove(engine)
# car.show()
