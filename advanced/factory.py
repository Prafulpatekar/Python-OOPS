# Abstraction in python 
# you can't create instance of an Abstract class can inheritate
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """ Interface Method """
    
class Student(IPerson):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Basic Student Name"
    
    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")
    
# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if str(person_type).capitalize() == "Student":
            return Student()
        if str(person_type).capitalize() == "Teacher":
            return Teacher()
        raise TypeError

if __name__=="__main__":
    _type = input("Enter person type to create object\n")
    person = PersonFactory.build_person(_type)
    person.person_method()