class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Square(Parallelogram):
    def get_area(self):
        return self.width ** 2
