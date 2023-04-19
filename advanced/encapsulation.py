# Encapsulation: Don't want to give direct access
class Person:
    def __init__(self,name,age,gender) -> None:
        self.__name = name # '__' (Double underscore) means private attribute
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self,value):
        if len(value) > 0:
            self.__name = value

    @property
    def Age(self):
        return self.__age
    
    @Age.setter
    def Age(self,value):
        if value > 0:
            self.__Age = value

    @property
    def Gender(self):
        return self.__gender
    
    @Gender.setter
    def Gender(self,value):
        if str(value) == 'M' or value == 'F':
            self.__gender = value
    

p1 = Person("Praful",23,"M")
if __name__=="__main__":
    print(p1.Name)
    print(p1.Age)
    print(p1.Gender)
    p1.Name = "Patekar"
    print(p1.Name)
