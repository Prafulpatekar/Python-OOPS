class Person:
    def __init__(self,name,age) -> None:
        # Constructor
        self.name = name
        self.age = age
    
    def __del__(self):
        # Destructor
        print("Object is destructed")
    

class Vector:
    def __init__(self,x,y) -> None:
        # Constructor
        self.x = x
        self.y = y

    def __add__(self,other):
        # Operator Overloading
        return Vector((self.x + other.x), (self.y + other.y))

    def __repr__(self) -> str:
        # Object Representation
        return f"X: {self.x}, Y:{self.y}"

    def __call__(self):
        # Object Call method
        return f"Vector {self.__repr__()} is called"
    
# person1 = Person("Praful",23)
vec1 = Vector(22,23)
vec2 = Vector(52,30)
vec3 = vec1 + vec2
print(vec3.x ,vec3.y)# Operator Overloading
print(vec3())
