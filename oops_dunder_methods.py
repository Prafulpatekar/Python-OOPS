# Dunder / Magic Methods str>>repr

class Employee:
    num_of_emps = 0
    def __init__(self,name,last,pay) -> None:
        self.name = name
        self.last = last
        self.pay = pay
        self.email = f"{name}.{last}@gmail.com"
        Employee.num_of_emps += 1
    
    def fullName(self)-> str:
        return f"{self.name} {self.last}"
    

    def __repr__(self) -> str:
        return f"Employee('{self.name}','{self.last}',{self.pay})"
    
    def __str__(self) -> str:
        return f"{self.fullName()} has pay of {self.pay} & can connect on email {self.email}"
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullName())


if __name__=="__main__":
    emp1 = Employee('Praful','Patekar',36000)
    emp2 = Employee('Harsh','Patekar',50000)
    
    print(emp2)
    print(emp1.pay)
    
    print(Employee.__dict__)
    print(emp1.__dict__)

    print(emp2)
    print(emp2.__repr__())
    print(emp2.__str__())
    print(repr(emp1))
    print(str(emp1))

    print(emp1 + emp2)
    print(len(emp1))


