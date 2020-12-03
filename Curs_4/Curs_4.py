class Coordinate(object):
    """ O coordonata este compusa din valorile x si y """

    def __init__(self, x, y):
        """ Setam valorile pentru x si y """
        self.x = x
        self.y = y

    def __str__(self):
        """ Afisam coordonatele x si y """
        return f"<{self.x}, {self.y}>"

    def distance(self, other: "Coordinate"):
        """ Returneaza distanta euclidiana dintre 2 coordonate """
        x_difference_squared = (self.x - other.x) ** 2
        y_difference_squared = (self.y - other.y) ** 2
        return (x_difference_squared + y_difference_squared) ** 0.5


origin = Coordinate(0, 0)
print(id(origin))
print(origin)
print(origin.x)

c1 = Coordinate(1, 0)
c2 = Coordinate(0, 2)

print(c1)
print(c2)
print(origin.distance(origin))
print(c1.distance(origin))
print(c2.distance(origin))
print(c1.distance(c2))
