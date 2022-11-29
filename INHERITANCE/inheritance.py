class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Person1(Person):
    def __init__(self, firstname, lastname, age, graduation):
        super().__init__(firstname, lastname, age)
        self.graduation = graduation


p1 = Person1("Patrick", "NDAYAMBAJE", 20, 2022)
print(p1.graduation)
