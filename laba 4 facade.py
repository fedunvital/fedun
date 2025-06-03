class Conveyor:
    def set_body(self):
        print('Body set!')

    def set_engine(self):
        print('Engine set!')

    def set_interior(self):
        print('Exterior added!')

    def set_exterior(self):
        print('Added interior!')

    def set_wheels(self):
        print('Wheels!')

    def add_electronics(self):
        print('Added electronics!')

    def paint(self):
        print('Car painted!')


class ConveyorFacade:
    def __init__(self, car: Conveyor):
        self.car = car

    def assemble_car(self):
        self.car.set_body()
        self.car.set_engine()
        self.car.set_interior()
        self.car.set_exterior()
        self.car.set_wheels()
        self.car.add_electronics()
        self.car.paint()


# Використання
conveyor = Conveyor()
facade = ConveyorFacade(conveyor)
facade.assemble_car()
