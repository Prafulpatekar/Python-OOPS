from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """ Interface Method """
    
class Person(IPerson):

    def person_method(self):
        print("I am a person")

class ProxyPerson(IPerson):

    def __init__(self) -> None:
        super().__init__()
        self.person = Person()  
        # self.name = "Basic Person Name"
    
    def person_method(self):
        print("I am proxyperson ")
        self.person.person_method()
        # Before and after can do anything

if __name__=="__main__":
    p1 = Person()
    p1.person_method()
    p2 = ProxyPerson()
    p2.person_method()