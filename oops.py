# Class, Objects and Methods
# Class variables : check instance>class>inherit class
# Classmethods
# Static Methods
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

    @classmethod
    def set_raise_amt(cls,amt)->None:
        cls.raise_amt = amt

    @classmethod
    def from_string(cls,string):
        # Alternate Constructor
        name,last, pay = string.split('-')
        return cls(name,last,pay)

    @staticmethod
    def is_weekday(day)->None:
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

    def __str__(self) -> str:
        return f"{self.fullName()} has pay of {self.pay} & can connect on email {self.email}"

emp1 = Employee('Praful','Patekar',36000)
emp2 = Employee('Harsh','Patekar',33000)

str1='Sachin-Patel-30000'
new_emp = Employee.from_string(str1) # calling class method

import datetime
my_date = datetime.date(2023,4,12)

if __name__=="__main__":
    print(Employee.num_of_emps)
    # print(emp2)
    # print(emp1.pay)
    # Employee.applyRaise(emp1)
    # print(emp1.pay)
    # print(Employee.__dict__)
    # print(emp1.__dict__)
    # Employee.set_raise_amt(1.06)
    # print(Employee.raise_amt)
    # print(emp1.raise_amt)
    # print(emp2.raise_amt)
    # print(new_emp)
    print(Employee.is_weekday(my_date))


