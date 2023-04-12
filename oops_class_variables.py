# Class variables : instance>class>inherit class

class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self,name,last,pay) -> None:
        self.name = name
        self.last = last
        self.pay = pay
        self.email = f"{name}.{last}@gmail.com"
        Employee.num_of_emps += 1
    
    def fullName(self)-> str:
        return f"{self.name} {self.last}"
    
    def applyRaise(self)-> None:
        # self.pay = float(self.pay) * float(Employee.raise_amt) # can change amt for whole class
        self.pay = float(self.pay) * float(self.raise_amt) # Can change raise amt for instance also any sub class can overwrite

    def __str__(self) -> str:
        return f"{self.fullName()} has pay of {self.pay} & can connect on email {self.email}"
    

if __name__=="__main__":
    emp1 = Employee('Praful','Patekar',36000)
    emp2 = Employee('Harsh','Patekar',50000)

    import datetime
    my_date = datetime.date(2023,4,12)

    print(Employee.num_of_emps)
    print(emp2)
    print(emp1.pay)
    Employee.applyRaise(emp1)
    print(emp1.pay)
    print(Employee.__dict__)
    print(emp1.__dict__)
    print(Employee.raise_amt)
    print(emp1.raise_amt)
    print(emp2.raise_amt)
    



