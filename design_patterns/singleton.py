"""
Pattern Name - Singleton
Pattern Type - Creational Design Pattern
"""
# Solution 1
class SingleTon(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

obj_1 = SingleTon()
print("Object_1 ==> ",obj_1)
obj_1.data = 10

obj_2 = SingleTon()
print("Object_2 ==> ",obj_2)
print("Object_2 data ==> ",obj_2.data)
obj_2.data = 5

print("Object_1  data ==> ",obj_1.data)

# Solution 2
class Borg(object):
    _shared = {}
    def __init__(self) -> None:
        self.__dict__ = self._shared

class SingleTon(object):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name

o1 = SingleTon("Praful")
print("Object 1 ==>",o1)
print("Object 1 ==>",o1.name)

o2 = SingleTon("Harsh")
print("Object 2 ==>",o2)
print("Object 2 ==>",o2.name)
print("Object 1 ==>",o1.name)

print(o1.__dict__)
print(o2.__dict__)

# Solution 3
from typing import Any


class SingleTonDecorator(object):
    def __init__(self,klass) -> None:
        self.klass = klass
        self.instance = None

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance

@SingleTonDecorator
class Logger(object):
    def __init__(self) -> None:
        self.start = None

    def write(self,message):
        if self.start:
            print(f"{self.start} {message}")
        else:
            print(message)

o1 = Logger()
o1.start ="[0] =>"
o1.write("Hellow")
o2 = Logger()
o2.start ="[1] =>"
o1.write("Hellow Object 2")

# Solution - 4
class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        print(cls.__instances)
        return cls.__instances[cls]


class DBConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "Not Connected"

    def disconnect(self):
        self.status = "Disconnected"

    def connect(self):
        self.status = "Connected"


client1 = DBConnector()
print("Client 1 ", client1)
print(client1.status)

client2 = DBConnector()
print("Client 2 ", client2)
client2.connect()
print(client1.status)

client1.disconnect()
print(client2.status)
