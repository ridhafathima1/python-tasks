#example of inserting manually in a normal list
# num=[10,20,30,40,50]
# position=4
# value=45
# num.append(0)
# for i in range(len(num)-1,position,-1):
#     num[i]=num[i-1]
# num[position]=value
# print(num)

#example of delete manually from a normal list
# num=[10,20,30,40]
# position=2
# for i in range(position,len(num)-1):
#     num[i]=num[i+1]
# num.pop()    
# print(num)    

#example of reversing manually in anormal list
# num=[10,20,30,40,50,60]
# start=0
# end=len(num)-1

# while start<end:
#     num[start],num[end]=num[end],num[start]
#     start+=1
#     end-=1
# print(num)

#example of searching manually in a normal list
# num=[10,20,30,40,50,60]
# target=500
# for i in range(len(num)):
#     if num[i]==target:
#         print("the element is found at index:",i)
#         break
# else:
#     print("the element is not found")

#example of deepcopy
# import copy
# num=[[10,20],[30,40]]
# deep=copy.deepcopy(num)
# deep[0][0]=100
# print(deep)
# print(num)

#example of shallowcopy
# import copy
# num=[[10,20],[30,40]]
# shallow=copy.copy(num)
# shallow[0][1]=200
# print(shallow)
# print(num)

#singly linked list insertion at the beginning
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertbeginning(self,data):
#         newnode=Node(data)
#         newnode.next=self.head
#         self.head=newnode
#     def insertend(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode 
#     def insert_position(self,data,position):
#         newnode=Node(data)
#         if position==0:
#             self.head=newnode
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             newnode.next=current.next
#             current.next=newnode  
#     def delete_first(self):
#         self.head=self.head.next  
#     def delete_end(self):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             self.head=None
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#     def dlete_position(self,position):
#         if position==0:
#             self.head=self.head.next
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             current.next=current.next.next                                              
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insertbeginning(10)                            
# l.insertbeginning(20)                            
# l.insertbeginning(30)                            
# l.insertbeginning(40)
# l.insertend(50)
# l.insertend(60)
# l.insertend(70)
# l.insertend(80)
# l.insert_position(100,3)
# l.delete_first()
# l.delete_end()
# l.dlete_position(1)
# l.display()                           

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_first(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             newnode.next=self.head
#             self.head.prev=newnode
#             self.head=newnode
#     def insert_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             newnode.prev=current
#             current.next=newnode    
#     def insert_position(self,data,position):
#         newnode=Node(data)
#         if position==0:
#             self.head=newnode
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             newnode.prev=current
#             newnode.next=current.next
#             current.next=newnode
#             current.next.prev=newnode    
#     def deletebegin(self):
#         self.head=self.head.next
#         self.head.prev=None
#     def deleteend(self):
#         current=self.head
#         while current.next:
#             current=current.next
#         current.prev.next=None 
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next
#         if current.next:
#             current.next.prev=current    
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insert_first(10)                       
# l.insert_first(20)                       
# l.insert_first(30)                       
# l.insert_first(40)
# l.insert_end(50)
# l.insert_end(60)
# l.insert_end(70)
# l.insert_end(80)     
# l.insert_position(100,2)
# l.deletebegin() 
# l.deleteend()  
# l.delete_position(3)
# l.display()               


# #example of factorial using recursion 
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

#example of fibonacci using recursion
# def fibonnacci(n):
#     if n<=1:
#         return n
#     return fibonnacci(n-1)+fibonnacci(n-2)
# for i in range(7):
#     print(fibonnacci(i),end=" ") 

#example of reversing using recursion
# def reverse(n):
#     if len(n)==0:
#         return n
#     return reverse(n[1:])+n[0]
# print(reverse("my name is ridha fathima"))

#example of liner search
# num=[1032,56,32,76,87]
# target=76
# for i in range(len(num)):
#     if num[i]==target:
#         print("the element id found at index:",i)
#         break
# else:
#     print("the element is not found")

#example of binary search
# num=[10,20,30,40,50,60,70]
# target=200
# low=0
# high=len(num)-1
# while low<high:
#     mid=(low+high)//2
#     if num[mid]==target:
#         print("the element is found at index:",mid)
#         break
#     elif num[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# else:
#     p
# 
#print("the element is not found")


#example of bubble sort
# num=[10,40,52,54,86,90,21]
# n=len(num)
# for i in range(n):
#     for j in range(n-i-1):
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]
# print(num)            

#example of selection sort
# num=[78,54,53,52,61,67,68,69]
# n=len(num)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if num[j]<num[min_index]:
#             min_index=j
#     num[i],num[min_index]=num[min_index],num[i]
# print(num)        

#example of insertion sort
#num=[43,54,65,76,87,98,32,21,21]
# n=len(num)
# for i in range(1,n):
#     key=num[i]
#     j=i-1
#     while j>=0 and num[j]>key:
#         num[j+1]=num[j]
#         j-=1
#     num[j+1]=key
# print(num)   

#example of stack operations 
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         self.stack.pop()
#     def peek(self):
#         print("the top element is",self.stack[-1])
#     def display(self):
#         print(self.stack)
# s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.pop()
# s.peek()
# s.display()

#singly linked list operations
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_first(self,data):
#         newnode=Node(data)
#         newnode.next=self.head
#         self.head=newnode
#     def insert_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#            self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode 
#     def insert_position(self,data,position):
#         newnode=Node(data)
#         if position==0:
#             self.head=newnode
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             newnode.next=current.next
#             current.next=newnode  
#     def delete_first(self):
#         self.head=self.head.next   
#     def delete_end(self):    
#         current=self.head
#         while current.next.next:
#             current=current.next
#         current.next=current.next.next
#     def delete_position(self,position):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             self.head=self.head.next
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             current.next=current.next.next        
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insert_first(10)
# l.insert_first(20)
# l.insert_first(30)                           
# l.insert_first(40)
# l.insert_end(50)
# l.insert_end(60)
# l.insert_end(70)
# l.insert_end(80)
# l.insert_position(100,3)
# l.delete_first()
# l.delete_end()
# l.delete_position(1)
# l.display()

#operations of doubly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_first(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             newnode.next=self.head
#             self.head.prev=newnode
#             self.head=newnode
#     def insert_end(self,data):
#         newnode=Node(data)
#         current=self.head
#         while current.next:
#             current=current.next
#         newnode.prev=current
#         current.next=newnode   
#     def insert_position(self,data,position):
#         current=self.head
#         newnode=Node(data)
#         for i in range(position):
#             current=current.next
       
#         newnode.next=current.next
#         newnode.prev=current
#         current.next.prev=newnode 
#         current.next=newnode
#     def delete_first(self):
#         self.head=self.head.next
#         self.head.prev=None    
#     def delete_end(self):
#         current=self.head
#         while current.next:
#             current=current.next
#         current.prev.next=None
#         current.next=None 
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next
#         if current.next:
#             current.prev.next=current                          
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insert_first(10)
# l.insert_first(20)
# l.insert_first(30)
# l.insert_end(40)
# l.insert_end(50)
# l.insert_end(60)
# l.insert_position(100,2)
# l.delete_first()
# l.delete_end()
# l.delete_position(2)
# l.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def convert(self,numbers):
        for i in numbers:
            newnode=Node(i)
            if self.head is None:
                self.head=newnode
            else:
                current=self.head
                while current.next:
                    current=current.next
                current.next=newnode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next          
numbers=[10,20,30,40,50]                   
l=Linkedlist()
l.convert(numbers)
l.display()
    
