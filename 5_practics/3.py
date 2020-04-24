class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sum__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return ('Равны')
        else:
            return ('Не равны')