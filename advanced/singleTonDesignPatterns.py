# Singleton design patter will only have one object
from abc import ABCMeta,abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data(self):
        """ Implement in Child Class """

class PersonSingleton(IPerson):
    __instance = None
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance==None:
            PersonSingleton("Default Name",0)
        return PersonSingleton.__instance

    def __init__(self,name,age) -> None:
        if PersonSingleton.__instance !=None:
            raise SystemError("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"I am person singleton Name:{PersonSingleton.__instance.name}")
if __name__=="__main__":
    p1 = PersonSingleton("Praful Patekar",23)
    p1.print_data()
    # p2 = PersonSingleton("JJS",5)
    # p2.print_data()
