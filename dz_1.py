class Car:
    def __init__(self, brand, color, engine_capacity):
        brand = brand
        color = color
        engine_capacity = engine_capacity

    def go_forward(self):
        print("The car is moving forward.")

    def go_backward(self):
        print("The car is moving backward.")


class AdvancedCar(Car):
    def turn_right(self):
        print("The car is turning right.")

    def turn_left(self):
        print("The car is turning left.")

