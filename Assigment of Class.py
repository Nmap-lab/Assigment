#To create python class
class Person:
    #constructor
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    #method
    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and my gender is {self.gender}."
 
 #Object
info=Person('saidi', 28, 'Me')

print("Person information is: ",info.introduce())






