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

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            newnode.prev=current
            current.next=newnode    
    def insert_position(self,data,position):
        newnode=Node(data)
        if position==0:
            self.head=newnode
        else:
            current=self.head
            for i in range(position-1):
                current=current.next
            newnode.prev=current
            newnode.next=current.next
            current.next=newnode
            current.next.prev=newnode    
    def deletebegin(self):
        self.head=self.head.next
        self.head.prev=None
    def deleteend(self):
        current=self.head
        while current.next:
            current=current.next
        current.prev.next=None 
    def delete_position(self,position):
        current=self.head
        for i in range(position-1):
            current=current.next
        current.next=current.next.next
        if current.next:
            current.next.prev=current    
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
l=Linkedlist()
l.insert_first(10)                       
l.insert_first(20)                       
l.insert_first(30)                       
l.insert_first(40)
l.insert_end(50)
l.insert_end(60)
l.insert_end(70)
l.insert_end(80)     
l.insert_position(100,2)
l.deletebegin() 
l.deleteend()  
l.delete_position(3)
l.display()               