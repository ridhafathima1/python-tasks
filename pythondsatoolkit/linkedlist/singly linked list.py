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

  # class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# print(n1.data)
# print(n1.next)        