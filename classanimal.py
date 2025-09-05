# import necessary packages
from abc import ABC, abstractmethod
# create a base classs
class Animal(ABC):

    # abstract method
    # should be implement by all sub-classes
    def move(self):
        pass

# sub class
class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can back")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

# driver code 
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()