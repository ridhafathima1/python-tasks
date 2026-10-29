#print("hello,python!")
#name=input("enter your name:")
#print("welcome",name)

#example of encanpsulation
# class Student:
#     def __init__(self,name,age,):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("my name is ",self.name)
#         print("iam",self.age,"years old")
# student=Student("ridha",17)
# student.display()
#  #example of abstraction
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Bike(Vehicle):
#     def start(self):
#         print("the bike start using key")
# class Car(Vehicle):
#     def start(self):
#         print("the car start using button")
# bike=Bike()
# car=Car()
# bike.start()
# car.start()                
# #example of inheritance
# class Animal:
#     def eat(self):
#         print("the animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("the dog is barking")
# dog=Dog()
# dog.eat()
# dog.bark()  
# #example of polymorphism             
# class Dog:
#     def sound(self):
#         print("the dog is barking")
# class Cat:
#     def sound(self):
#         print("the cat is meowing")
# cat=Cat()
# dog=Dog()
# cat.sound()
# dog.sound()                
# #example of variables and datatypes
# name="ridha"
# age=17
# percentage=99.4
# passed=True
# print(type(name))
# print(type(age))
# print(type(percentage))
# print(type(passed))
# #example of type conversion
# num=input("enter a number:")
# print("original value:",num)
# print("original type:",type(num))
# convert=int(num)
# print("converted value:",convert)
# print("converted type:",type(convert))
# print("square:",convert*convert)
# #example of arithmetic operatos
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# print("sum:",num1+num2)
# print("difference:",num1-num2)
# print("product:",num1*num2)
# print("division:",num1/num2)
# print("floor division:",num1//num2)
# print("remainder:",num1%num2)
# print("power:",num1**num2)
#example of conditional statements
# num=int(input("ennter your mark:"))
# if num>=90 and num<=100:
#     print("grade A")
# elif num>=80 and num<=89:
#     print("grade b")
# elif num>=70 and num<=79:
#     print("grade c")
# elif num>=50 and num<=69:
#     print("grade d")
# elif num<50:
#     print("failed")    
# example of loop print 1 to 10
# for i in range(1,11):
    # print(i)
i=1
while i<=10:
    print(i)
    i+=1
