#print("hello,python!")
#name=input("enter your name:")
#print("welcome",name)

#example of encanpsulation
class Student:
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def display(self):
        print("my name is ",self.name)
        print("iam",self.age,"years old")
student=Student("ridha",17)
student.display()
 #example of abstraction
from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("the bike start using key")
class Car(Vehicle):
    def start(self):
        print("the car start using button")
bike=Bike()
car=Car()
bike.start()
car.start()                
#example of inheritance
class Animal:
    def eat(self):
        print("the animal is eating")
class Dog(Animal):
    def bark(self):
        print("the dog is barking")
dog=Dog()
dog.eat()
dog.bark()               