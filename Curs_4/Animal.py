class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"animal: {self.name} | {self.age}"


class Cat(Animal):
    def speak(self):
        print("meow meow")

    def __str__(self):
        return f"cat = {self.name} | {self.age}"


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def speak(self):
        print("Hello")

    def get_friends(self):
        return ", ".join(self.friends)

    def add_friend(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def age_diff(self, other_person:"Person"):
        diff = self.age - other_person.age
        print(f"{abs(diff)} years difference")

    def __str__(self):
        return f"Person: {self.name} | {self.age}"

    def __sub__(self, other):
        return abs(self.age - other.age)


class Rabbit(Animal):
    # class variable
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return self.rid

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        # copilul iepurilor
        return Rabbit(0, self, other)

    def __str__(self):
        return f"rabbit: {self.rid}"

    def __eq__(self, other):
        try:
            same_parents = (self.parent1.get_rid == other.parent1.get_rid() and
                            self.parent2.get_rid == other.parent2.get_rid())
            opposite_parents = (self.parent1.get_rid() == other.parent2.get_rid() and
                                self.parent2.get_rid() == other.parent1.get_rid())
            return same_parents or opposite_parents
        except Exception as e:
            print("Nu ai parinti ", e)

r1 = Rabbit(10)
r2 = Rabbit(20)

print(r1.get_rid())
print(r2.get_rid())

r3 = Rabbit(10)
r4 = Rabbit(20)

r5 = r1 + r2
r55 = r2 + r1

r6 = r3 + r4
r66 = r4 + r3

print(r5)
print(r6)

print(f"Parent 1 is {r5.get_parent1()}")
print(f"Parent 2 is {r5.get_parent2()}")

print(f"Parent 1 is {r6.get_parent1()}")
print(f"Parent 2 is {r6.get_parent2()}")

print(r5 == r55)
print(r6 == r66)
print(r5 == r6)
print(r1 == r2)
# Ion = Person("Ion", 30)
# Ana = Person("Ana", 28)
# Vasile = Person("Vasile", 10)
#
# print(Ion)
# print(Ana)
# Ana.add_friend("Ion")
# Ana.add_friend("Vasile")
# Ana.add_friend("Maria")
# Ana.add_friend("Maria")
# print(Ana.get_friends())
# Ion.speak()
# Ana.age_diff(Ion)
# print(Ion - Ana)
# print(Vasile - Ana)
#
# dog = Animal(4)
# print(dog)
# dog.set_name("Azorel")
# dog.set_age(10)
# print(dog)
#
# tom = Cat(4)
# print(tom)
#
# tom.set_name("Tom")
# print(tom.get_name())
# print(tom)
