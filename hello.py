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


