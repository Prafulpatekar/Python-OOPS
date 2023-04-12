# Property Decorators
# Getter and setter

class Employee:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last
    
    @property
    def email(self)-> str:
        return f"{self.name}.{self.last}@gmail.com"
    
    @property
    def fullName(self)-> str:
        #"GETTER"
        return f"{self.name} {self.last}"
    
    @fullName.setter
    def fullName(self,newName):
        #"SETTER"
        self.name , self.last = str(newName).split(' ')

    @fullName.deleter
    def fullName(self):
        "deleter"
        print("Delete Name!")
        self.name,self.last = None,None

    def __repr__(self) -> str:
        return f"Employee('{self.name}','{self.last}')"
    
    def __str__(self) -> str:
        return f"{self.fullName()} can connect on email {self.email}"
    


if __name__=="__main__":
    emp1 = Employee('Praful','Patekar')
    emp2 = Employee('Harsh','Patekar')
    print(emp2.email)
    print(emp2.fullName)
    emp2.name = 'Pawan'
    emp2.fullName = 'Pawan Kumar'

    print(emp2.email)
    print(emp2.fullName)
    del emp1.fullName
    


   
   


