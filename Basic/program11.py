class Person:
    def __init__(self, name, age):
        self.__name = name     # private attribute
        self.__age = age       # private attribute

    def display_info(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

p = Person("Alice", 25)
print(p.display_info())


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())