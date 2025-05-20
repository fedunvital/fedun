import copy


class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Авто: {self.brand} {self.model}, колір: {self.color}")

# Головна функція
def main():
    original_car = Car("Civic", "Honda", "червоний")
    print("Оригінал:")
    original_car.display()

    # Клонуємо об'єкт
    cloned_car = original_car.clone()
    cloned_car.color = "синій"   

    print("\nКлон (з іншим кольором):")
    cloned_car.display()

# Запуск
if __name__ == "__main__":
    main()
