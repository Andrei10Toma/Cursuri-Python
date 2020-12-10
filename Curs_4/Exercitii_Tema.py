class Fraction(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            print("The denominator can't be 0")
            exit(-2)
        elif denominator < 0:
            self.numerator = (-1) * numerator
            self.denominator = (-1) * denominator
        else:
            self.numerator = numerator
            self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, new_numerator):
        self.numerator = new_numerator

    def set_denominator(self, new_denominator):
        self.denominator = new_denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)


if __name__ == '__main__':
    fraction_1 = Fraction(-3, -2)
    fraction_2 = Fraction(1, -2)
    print(f"First fraction: {fraction_1}")
    print(f"Second fraction: {fraction_2}")
    fraction_3 = fraction_1 + fraction_2
    print(f"Sum of first and second fraction:{fraction_3}")
    fraction_3 = fraction_1 - fraction_2
    print(f"Sub of first and second function: {fraction_3}")
    fraction_1_inverse = fraction_1.inverse()
    fraction_2_inverse = fraction_2.inverse()
    print(f"First fraction reversed: {fraction_1_inverse}")
    print(f"Second fraction reversed: {fraction_2_inverse}")
