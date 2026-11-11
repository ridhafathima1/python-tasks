# converting python list to linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# numbers=[1,2,3,4,5,7]
# head=None
# tail=None
# for num in numbers:
#     newnode=Node(num)
#     if head is None:
#         head=newnode
#         tail=newnode
#     else:
#         tail.next=newnode
#         tail=newnode
# current=head
# while current:
#     print(current.data)
#     current=current.next        

# # converting linkedlist into python list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# node1.next=node2
# node2.next=node3
# node3.next=node4
# head=node1
# numbers=[]
# current=head
# while current:
#     numbers.append(current.data)
#     current=current.next

# print(numbers)

#simple singly linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node1.next=node2
# node2.next=node3
# head=node1
# current=head
# while current:
#     print(current.data)
#     current=current.next

#singly linkedlist insertion at the beginning
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node1.next=node2
# node2.next=node3
# head=node1
# values=[10,20,30,40,50]
# for value in reversed(values):
#     newnode=Node(value)
#     newnode.next=head
#     head=newnode
# current=head
# while current:
#     print(current.data)
#     current=current.next 
     
#insert at the beginning of singly linkedlist another method
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def addfirst(self,data):
#         newnode=Node(data)
#         newnode.next=self.head
#         self.head=newnode
#     def display(self):
#         current=self.head
#         while current is not None:
#             print(current.data)
#             current=current.next                                       
# l1=Linkedlist()
# l1.addfirst(10)
# l1.addfirst(20)
# l1.addfirst(30)
# l1.display()
#insert at the end in d=singly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def addend(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.addend(10)
# l.addend(20)
# l.addend(30)
# l.display()            

#simple example of node
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# print(n1.data)
# print(n1.next)        

#simple example of node
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n1.next=n2
# head=n1
# current=head
# while current:
#     print(current.data)
#     current=current.next

#example create and display a linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n1.next=n2
# n2.next=n3
# n3.next=n4
# head=n1
# current=head
# while current is not None:
#     print(current.data)
#     current=current.next

#count number of nodes
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n1.next=n2
# n2.next=n3
# n3.next=n4
# head=n1
# current=head
# count=0
# while current is not None:
#     count+=1
#     current=current.next
# print("total nodes:",count)

#search a node
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n1.next=n2
# n2.next=n3
# n3.next=n4
# head=n1
# search=30
# found=False
# current=head
# while current is not None:
#     if current.data==search:
#         found=True
#         break
#     current=current.next
# if found:
#     print("element is found")
# else:
#     print("element not found")        

#insert at the beginning
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_beginning(self,data):
#         newnode=Node(data)
#         newnode.next=self.head
#         self.head=newnode
#     def display(self):
#         current=self.head
#         while current is not None:
#             print(current.data)
#             current=current.next
# l1=Linkedlist()
# l1.insert_beginning(30)
# l1.insert_beginning(20)
# l1.insert_beginning(10)
# l1.display()      

#insert at the ending
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode
#     def display(self):
#         current=self.head
#         print(current.data) 
#         current=current.next
# l=Linkedlist()
# l.insert_end(10)
# l.insert_end(20)
# l.insert_end(30)
# l.display()                           


# #insert at a particular position
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_position(self,data,position):
#         newnode=Node(data)
#         if position == 0:
#             newnode.next=self.head
#             self.head=newnode
#             return
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         newnode.next=current.next
#         current.next=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insert_position(10,0)
# l.insert_position(20,1)
# l.insert_position(30,2)
# l.insert_position(30,1)  
# l.display()          
                 
#delete from frromt the beginning singly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode
#     def deletebeginning(self):
#         if self.head is None:
#             print("the list is empty")
#         else:
#             self.head=self.head.next
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insert_end(10)
# l.insert_end(20)
# l.insert_end(30)
# l.deletebeginning()
# l.display()                                         

#delete the end elemen t in singgly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def deleteend(self):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             self.head=None
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# l.head=n1
# n1.next=n2
# n2.next=n3
# l.deleteend()
# l.display()                                    
 
#delete specific position from singly linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def deletespecific(self,position):
#         if self.head is None:
#             return 
#         if position == 0:
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
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# l.head=n1
# n1.next=n2
# n2.next=n3
# l.deletespecific(1)
# l.display()             

#insert at the beginning ending and a specific position entire code
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertbegin(self,data):
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
#     def insertposition(self,data,pos):
#         newnode=Node(data)
#         if pos == 0:
#             self.head=newnode
#         else:
#             current=self.head
#             for i in range(pos-1):
#                 current=current.next
#             newnode.next=current.next
#             current.next=newnode    
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insertbegin(20)
# l.insertbegin(10)

# l.insertend(40)
# l.insertend(50)

# l.insertposition(30,2)
# l.display()   

#complete delete operatios in singly linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode    
#     def deletebegin(self):
#         if self.head is None:
#             print("the list is empty")
#         else:
#             self.head=self.head.next
#     def deleteend(self):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             self.head=None
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#     def deletespecfic(self,pos):
#         if self.head is None:
#             return 
#         if pos==0:
#             self.head=self.head.next
#         else:
#             current=self.head
#             for i in range(pos-1):
#                 current=current.next
#             current.next=current.next.next
#     def display(self):
#         current=self.head 
#         while current:
#             print(current.data)
#             current=current.next       
# l=Linkedlist()
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n5=Node(50)
# l.head=n1
# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5
# l.deletebegin()
# l.deleteend()
# l.deletespecfic(1)
# l.display()     

#example of bubble sort
# numbers=[1,10,7,5,3,0]
# n=len(numbers)
# for i in range(n):
#     for j in range(n-i-1):
#         if numbers[j]>numbers[j+1]:
#             numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
# print(numbers)                 

#example of insert at the beginning doubly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertbegin(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             newnode.next=self.head
#             self.head.prev=newnode
#             self.head=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insertbegin(30)
# l.insertbegin(20)
# l.insertbegin(10)
# l.display()                                 
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertbegin(self,data):
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
#     def insertspec(self,data,pos):
#         newnode=Node(data)
#         if pos == 0:
#             self.head=newnode
#         else:
#             current=self.head
#             for i in range(pos-1):
#                 current=current.next
#             newnode.next=current.next
#             current.next=newnode
#     def deletebegin(self):
#         if self.head is None:
#             print("the list is empty")
#         else:
#             self.head=self.head.next 
#     def deleteend(self):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             self.head=None
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#     def deletespec(self,pos):
#         if self.head is None:
#             return
#         if pos==0:
#             self.head=self.head.next
#         else:
#             current=self.head
#             for i in range(pos-1):
#                 current=current.next
              
#             current.next=current.next.next   

                   
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next   

# l=Linkedlist()
# l.insertbegin(30)
# l.insertbegin(20)
# l.insertbegin(10)
# l.insertend(40)
# l.insertend(50)
# l.insertend(60)
# l.insertspec(80,3)
# l.deletebegin()
# l.deleteend()
# l.deletespec(3)
# l.display()                 

#example of inserting at the end in douboy linked lists
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertend(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode
#             newnode.prev=current
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insertend(10)
# l.insertend(20)
# l.insertend(30)
# l.display()                                                          