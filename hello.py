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
class Student:
    def display(self):
        print("the student is hardworking")
    def new(self):
        print("the student is smart")
Student.display=Student.new
student=Student()
student.display()            
