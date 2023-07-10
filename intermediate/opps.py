class Person:

    def __init__(self,name,lastname,age) -> None:
        '''Constructor'''
        self.name = name
        self.lastname = lastname
        self.age = age
        Person.hands = 2

    def speak(self) -> None:
        '''method'''
        print(f"Hi, My name is {self.name} {self.lastname} and my age is {self.age}.")

    def __str__(self) -> str:
        '''dunder method will call at each print function call'''
        return f"Hi, My name is {self.name} {self.lastname} and my age is {self.age}."

class Worker(Person):
    def __init__(self, name, lastname, age,salary,maried) -> None:
        super().__init__(name, lastname, age)
        self.salary = salary
        self.is_maried = maried
    
    def __str__(self) -> str:
        return super().__str__() + f" Salary {self.salary} and Maritial Status {self.is_maried}"
    
    def calc_yearly_salary(self):
        return self.salary * 12

if __name__ == "__main__":
    praful = Worker("Praful","Patekar",23,36000,False)
    praful.speak()
    harsh = Worker("Harsh","Patekar",21,5000000,False)
    print(harsh.calc_yearly_salary())
    print(harsh)
