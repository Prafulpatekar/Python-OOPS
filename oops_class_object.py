# Class, Objects and Methods

class Employee:
    
    def __init__(self,name,last,pay) -> None:
        self.name = name
        self.last = last
        self.pay = pay
        self.email = f"{name}.{last}@gmail.com"
    
    def fullName(self)-> str:
        return f"{self.name} {self.last}"
    



if __name__=="__main__":
    emp1 = Employee('Praful','Patekar',36000)
    emp2 = Employee('Harsh','Patekar',50000)

    print(emp2)
    print(emp1.pay)
    print(Employee.__dict__)
    print(emp1.__dict__)



