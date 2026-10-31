                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #print("hello,python!") 
#name=input("enter your na  me:")
#pri    nt("welcome",name)

#example of encanpsu    lation
# class Student:    
#     def __init__(self,name    ,age,):
#         self.name=name    
#         self.age=age  
#     def display(self):    
#         print("my name is ",self.name)    
#         print("iam",self.age  ,"years old")
# student=Student("ridh a",17)
# st    udent.display()

#  #example of abstraction  
# from abc import ABC,ab    stractmethod
# class Vehicle(ABC):   
#     @abstractmethod   
#     def start(    self):
#         pass  
# class Bike(Vehicle):  
#     def start(self):  
#         print("the bik    e start using key")
# class Car(Vehicle):   
#     def start(self):  
#         print("   the car start using button")
# bike=Bike(    )
# car=Car() 
# bike.start()  
# ca    r.start()                

# #example of in    heritance
# class Animal: 
#     def eat(self):    
#         print("the ani    mal is eating")
# class Dog(Animal):    
#     def bark(self):   
#         pr    int("the dog is barking")
# dog=Dog() 
# dog.eat() 
# do    g.bark()  

# #example of po    lymorphism             
# class Dog:    
#     def sound(self):  
#         print(    "the dog is barking")
# class Cat:    
#     def sound(self):  
#         pr    int("the cat is meowing")
# cat=Cat() 
# dog=Dog() 
# cat.sound()   
# do    g.sound()                

# #example of vari  ables and datatypes
# name="ridh    a"
# age=17    
# percentage=99.    4
# passed=True   
# print(type(name)) 
# print(type(age))  
# print(type(percentage))   
# pr    int(type(passed))

# #example of type conversion   
# num=input("enter a number:")  
# print("original value:",num)  
# print("original ty    pe:",type(num))
# convert=int(num)  
# print("converted value:",convert) 
# print("converted type:",type(convert  ))
# pr    int("square:",convert*convert)

# #example of arithmetic operatos   
# num1=int(input("enter first number")) 
# num2=int(input("enter seco    nd number"))
# print("sum:",num1+num2)   
# print("difference:",num1-num2)    
# print("product:",num1*num2)   
# print("division:",num1/num2)  
# print("floor division:",num1//    num2)
# print("remainder:",num1%num2) 
# pr    int("power:",num1**num2)

#example of conditional statements  
# num=int(input("ennter your m  ark:"))
# if num>=90 and num<=10    0:
#     print("grade A")  
# elif num>=80 and num<=    89:
#     print("grade b")  
# elif num>=70 and num<=    79:
#     print("grade c")  
# elif num>=50 and num<=69  :
#     print("gra    de d")
# elif num<50:  
#         print("failed")    

# example of loop print 1    to 10
# for i in range(1  ,11):
    # pr    int(i)
# i=1   
# while i<=10:  
#     print(i)  
#         i+=1

#example of even numbers fr om 2 to 20
# for i in range(2  ,21,2):
#         print(i)

#example     of sum of numbers
# sum=0 
# for i in range    (1,11):
#     sum+=i    
# pr    int("sum:",sum)

#example of mumltiplication table usin  g for loop
# num=int(input("enter a     number"))
# for i in range(1,11): 
        # print(num,"*",i,"=",num*i)

#example of length  
# num=input("enter a number")   
# pr    int(len(num.lstrip("-")))

#example of string reverse  
# text=input("enter a w ord:")
# pr    int(text[::-1])

#example of string reverse using    loop 
# text=input("en    ter a word:")
# reverse=""    
# for i in range(len(tex    t)-1,-1,-1):
#     reverse+=text[i]  
# pr    int(reverse)   

#example of palindrome or not   
# text=input("enter a wo    rd")
# if text==text[::-1]:  
#     pr    int("palindrome")
# else: 
#         print("not a palindrome")

#example of counting vowels 
# text=input    ("enter a word").lower()
# count=0   
# for i in text:    
#     if i in "aeiou    ":
#         count+=1  
# pr    int(count)        

#example of count consonants    
# text=input    ("enter a word:")
# count=0   
# for i in text:    
#     if i not in "a    eiou":
#         count+=1  
# pr    int(count)        

#example of remove spaces   
# text=input("enter a sentence  :")
# text=text.repla   ce(" ","")
# pr    int(text)

# example of count words in a stri  ng
# text=input("enter a s entence:")
# te    xt=text.split()

# pr    int(len(text))

#example of find largest number in a list    
# num=input("enter 5 numb   ers").split()
# largest=int(nu    m[0])
# for i in num: 
#     if int(i)>largest:    
#         largest=int(i)    
# pr    int("the largest number is:",largest) 

# example to find smallest number   
# num=input("enter 5 numbe  rs").split() 
# smallest=int(n    um[0])
# for i in num: 
#     if int(i)<smallest:   
#         smallest=int(i)   
# print("smallest number:",smallest)              
# num=input(    "enter 5  numbers").split()
# unique=[] 
# for i in num: 
#     if int(i) not in unique:  
#         unique.append(i   nt(i))
# pr    int(unique)      

#example to find prime number   
# num=int(input("enter a num    ber"))
# for i in range(2,n    um):
#     if num%i==0:  
#         print("no t prime")
#             break
# else: 
#         print("prime")

# num=int(input("enter a num    ber:"))
# for i in range(2,n    um):
#     if num%i==0:  
#         print("no t prime")
#             break
# else: 
#         print("prime")


# examples of tuple 
# numbers=(10,20,304,50)    
# print("length:",len(numbers)) 
# pr    int("largest number:",max(numbers))

# example of sets   
# numbers={10,20,30,40,1    0,20}
# print("set:",numbers) 
# print("number of u    nique elements",len(numbers))
# numbers.add(50)   
# pr    int("set after adding a number:",numbers)

# practical with dictionaries   
# def calculate_tota    l(a,b):
#     return a+b    
# result=calculate_total(5,6)   
# pr    int("sum is:",result)

# practical using lamba function
# square=lambda number:number**2
# result=square(5)
# print("square:",result)

# example of monkey patching
# class Student:
#     def display(self):
#         print("the student is hardworking")
#     def new(self):
#         print("the student is smart")
# Student.display=Student.new
# student=Student()
# student.display()            

#example of type of functions
#function without an argument and without a return value
# def greet():
#     print("my name is ridha fathima ")
# greet()    

# function with argument and withour return value
# def add(a,b):
#     print(a+b)
# add(300,80)    

#function without arguments and with a return value
# def num():
#     return 100
# result=num()
# print(result)


# function with arguments and a return value
# def sum(a,b):
#     return a+b
# print(sum(2,3))

# examples of magic methods
# example of magic method __init__
# class School:
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
# s1=School("fhss",1942)
# print(s1.name)
# print(s1.year)      

#example of magicmethod __str__
# class School:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"school name: {self.name}"
# s1=School("fhss")
# print(s1)

#example of magic method len()
# class Team:
#     def __init__(self,members):
#         self.members=members
#     def __len__(self):
#         return len(self.members)
# t1=Team(["ridha","raniya","rayan"])
# print(len(t1))

 # example of magic method __add__
# class Score:
#     def __init__(self,marks):
#         self.marks=marks
#     def __add__(self,other):
#         return self.marks+other.marks
# s1=Score(50)
# s2=Score(50)
# print(s1+s2)


# example of magic method __eq__       
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __eq__(self,others):
#         return self.name==others.name
# n1=Student("ridha")      
# n2=Student("ridha") 
# n3=Student("rayan")   
# print(n1==n2)
# print(n1==n3)

# def uppercase(func):
#     def wrapper():
#         result=func()
#         return result.upper()
#     return wrapper
# @uppercase
# def greet():
#     return "my name is ridha fathima"
# print(greet())

# # example of closure
# def outer():
#     message="my name is ridha fathima"
#     def inner():
#         print(message)
#     return inner
# greet=outer()
# greet()

# examples of functional programming tools
# example of map method
# numbers=[1,2,3,4,5,6]
# def square(n):
#     return n*n
# result=list(map(square,numbers))
# print(result)


#example of square of number using lambda
# numbers=[1,2,3,4,5,6]
# result=list(map(lambda n:n*n,numbers))
# print(result)

#example of filter normal and lambda
# numbers=[1,2,3,4,5,6]
# def even(n):
#     return n>2
# result=list(filter(even,numbers))
# print(result)

# numbers=[1,4,6,8,9]
# result=list(filter(lambda n:n>2,numbers))
# print(result)

# example of reduce normal and lambda 
# from functools import reduce
# numbers=[1,2,3,4,5,6]
# def add(a,b):
#     return a+b
# result=reduce(add,numbers)
# print(result)

# from functools import reduce
# numbers=[1,2,3,7,8,9]
# result=reduce(lambda a,b:a+b,numbers)
# print(result)

# example of zip normal and lambda
# numbers=[1,2,3,4]
# names=["ridha","raniya","rayan"]
# result=list(zip(numbers,names))
# print(result)

