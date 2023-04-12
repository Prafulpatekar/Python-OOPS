# Inheritance -> Multiple Inheritance
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
    

class Developer(Employee):
    raise_amt = 1.20

    def __init__(self, name, last, pay,skills) -> None:
        super().__init__(name, last, pay)
        self.skills = skills


class Manager(Employee):
    raise_amt = 1.02

    def __init__(self, name, last, pay,listOfEmps=None) -> None:
        super().__init__(name, last, pay)
        if listOfEmps is None:
            self.listOfEmps = []
        else:
            self.listOfEmps = listOfEmps

    def add_employee(self,emp):
        if emp not in self.listOfEmps:
            self.listOfEmps.append(emp)

    def remove_employee(self,emp):
        if emp in self.listOfEmps:
            self.listOfEmps.remove(emp)

    def get_emps(self):
        for idx,emp in enumerate(self.listOfEmps):
            print(f"{idx+1}) {emp.fullName()}")


if __name__=="__main__":
    emp1 = Employee('Praful','Patekar',36000)
    emp2 = Employee('Harsh','Patekar',50000)
    dev1 = Developer('Pratik','Nagpurkar',36000,['C++','CSS','HTML'])
    dev2 = Developer('Ayush','Hedaoo',36000,['C++','Java','Python'])
    manager1 = Manager('Sam','Parate',25000,[emp2,dev1,dev2])

    manager1.get_emps()
    manager1.add_employee(emp1)
    manager1.get_emps()
    manager1.remove_employee(emp2)
    manager1.get_emps()
    print(isinstance(manager1,Employee))# True
    print(isinstance(manager1,Manager))# True
    print(isinstance(manager1,Developer))# False
    print(issubclass(Manager,Employee))# True
    str1='Sachin-Patel-30000'
    new_emp = Employee.from_string(str1) # calling class method

    import datetime
    my_date = datetime.date(2023,4,12)

    print(Employee.num_of_emps)
    print(emp2)
    print(emp1.pay)
    Employee.applyRaise(emp1)
    print(emp1.pay)
    print(Employee.__dict__)
    print(emp1.__dict__)
    Employee.set_raise_amt(1.06)
    print(Employee.raise_amt)
    print(emp1.raise_amt)
    print(emp2.raise_amt)
    print(new_emp)
    print(Employee.is_weekday(my_date))
    print(help(Developer)) # Help To find Method Resolution Order

    print(dev1.pay)
    dev1.applyRaise()
    print(dev1.pay)
    print(dev1.skills)


