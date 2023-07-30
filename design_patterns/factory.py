"""
Pattern Name: Factory
Pattern Type: Creational Desgin Patten
helps to hide logic of creating object.
1. Simple Factory Pattern
2. Factory Method Pattern
3. Abstract Method Pattern
"""
from abc import ABCMeta, abstractmethod,ABC

class Person(ABC): # Important
    def __init__(self,name) -> None:
        super().__init__()
        self.create(name)

    @abstractmethod
    def create(self,name) -> None:
        pass

class HR(Person):
    def create(self,name) -> None:
        print(f"HR {name} is created")
class Employee(Person):
    def create(self,name) -> None:
        print(f"Employee {name} is created")


class PersonFactory(object):
    @classmethod
    def create_person(cls,designation,name):
        eval(designation)(name)


if __name__=="__main__":
    designation = input("Enter Designation ")
    name = input("Enter name ")
    PersonFactory.create_person(designation,name)