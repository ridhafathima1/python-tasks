#example of get duplicate values from a list using function
# def duplicate(num):
#     duplicates=[]
#     unique=[]
#     for i in num:
#         if i not in unique:
#             unique.append(i)
#         else:
#             duplicates.append(i)
#     return duplicates
# num=[10,20,30,40,30,40]
# result=duplicate(num)  
# print(result)       

#example to get second largest from a list using function
# def secondlargest(num):
#     largest=num[0]
#     second=num[0]
#     for i in num:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second and i!=largest:
#             second=i
#     return second
# num=[10,20,30,40,50]
# result=secondlargest(num)
# print(result)    

#example of reversing a list using function
# def reverselist(num):
#     start=0
#     end=len(num)-1
#     while start<end:
#         num[start],num[end]=num[end],num[start]
#         start+=1
#         end-=1
#     return num
# num=[10,20,30,40,50]
# result=reverselist(num)
# print(result)

#example of finding frequency using function
# def frequency(num):
#     frequency={}
#     for i in num:
#         if i in frequency:
#             frequency[i]+=1
#         else:
#             frequency[i]=1
#     return frequency
# num=[10,10,20,30,40,40,50,50,60,60]
# result=frequency(num)
# print(result)

#example of find duplicate values from a list using function
# def duplicate(num):
#     unique=[]
#     for i in num:
#         if i not in unique:
#             unique.append(i)
#     return unique
# num=[10,20,20,30,30,40,50]
# result=duplicate(num)
# print(result)

#example of stack operations
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,data):
#         self.stack.append(data) 
#     def pop(self):
#         print("pop element:",self.stack.pop())
#     def peek(self):
#         print("top element:",self.stack[-1])   
#     def display(self):
#         print(self.stack)
# s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.pop()
# s.peek()    
# s.display()    

#example of queue operations
# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,data):
#         self.queue.append(data)
#     def dequeue(self):
#         self.queue.pop(0)
#     def peek(self):
#         print("the top element is:",self.queue[-1])
#     def display(self):
#         print(self.queue)
# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.dequeue()
# q.peek()
# q.display() 

# from collections import deque
# d=deque([10,20,30])
# d.popleft()
# d.append(40)
# print(d)

#example of hasing 
# data={
#     "name":"ridha",
#     "age":17,
#     "course":"bca"
# }
# print(data["name"])
# if "age" in data:
#     print("age exists")
# del data["course"]
# print(data)    

#example of hash collision solution using hash function     
# data={
#     "name":"ridha",
#     "age":17,
#     "course":17
# }
# b=hash(17)
# a=hash(17)
# if a==b:
#     print("both are equal")
# del data["name"]
# print(data)

#example of linear search
# num=[10,20,30,40,50,43,4,2,4,]
# target=2
# for i in range(len(num)):
#     if num[i]==target:
#         print("the element is foudn at index:",i)
#         break
# else:
#     print("the element is not found")    

#example of binary search
# num=[10,20,30,40,50,60,70,80,90]
# target=40
# low=0
# high=len(num)-1
# while low<=high:
#     mid=(low+high)//2
#     if num[mid]==target:
#         print("the element is found at index:",mid)
#         break
#     elif num[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# else:
#     print("the element is not found")

# #example of bubble sort
# num=[2039,44,864,844,725,937]
# n=len(num)
# for i in range(n):
#     for j in range(n-i-1):
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]
# print(num)        
    
#example of selection sort
# num=[4049,498,30498,4494]
# n=len(num)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if num[j]<num[min_index]:
#             min_index=j
#     num[i],num[min_index]=num[min_index],num[i]
# print(num)

#example of insertion sort
# num=[308,5968,59686,5868]
# n=len(num)
# for i in range(n):
#     key=num[i]
#     j=i-1
#     while j>=0 and num[j]>key:
#         num[j+1]=num[j]
#         j-=1
#     num[j+1]=key
# print(num)    

#example of recursion using factorial
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

#example of fibanocci
# def fibanocci(n):
#     if n<=1:
#         return n
#     return fibanocci(n-1)+fibanocci(n-2)
# print(fibanocci(6))

#example of singly linked lis operations
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
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode   
#     def insert_position(self,data,position):
#         newnode=Node(data)
#         if position==0:
#             newnode.next=self.head
#             self.head-newnode
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             newnode.next=current.next
#             current.next=newnode  
#     def delete_first(self):
#         if self.head is None:
#             return
#         if self.head.next is not None:
#             self.head=self.head.next
#     def delete_end(self):
#         current=self.head
#         while current.next.next:
#             current=current.next
#         current.next=None  
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next                                     
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
# l.insert_first(50)
# l.insert_end(60)
# l.insert_end(70)
# l.insert_end(80)
# l.insert_end(90)
# l.insert_position(25,3)
# l.delete_first()
# l.delete_end()
# l.delete_position(4)
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
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         newnode.prev=current
#         newnode.next=current.next
#         current.next.prev=newnode
#         current.next=newnode  
#     def delete_first(self):
#         self.head=self.head.next
#         self.head.prev=None 
#     def delete_end(self):
#         current=self.head
#         while current.next:
#             current=current.next
#         current.next=None
#         current.prev.next=None
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next
#         if self.head is not None:
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
# l.insert_first(50)
# l.insert_end(60)
# l.insert_end(70)
# l.insert_end(80)
# l.insert_end(90)
# l.insert_end(100)
# l.insert_position(100,4)
# l.delete_first()
# l.delete_end()
# l.delete_position(4)
# l.display()                

#convert list to linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def convert(self,number):
#         for i in number:
#             newnode=Node(i)
#             if self.head is None:
#                 self.head=newnode
#             else:
#                 current=self.head
#                 while current.next:
#                     current=current.next
#                 current.next=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")    
# number=[2030,4049,409,495]
# l=Linkedlist()
# l.convert(number)                                        
# l.display()

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def display(self):
#         current=self.head
#         number=[]
#         while current:
#             number.append(current.data)
#             current=current.next
#         return number     
# l=Linkedlist()
# node1=Node(10)                        
# node2=Node(20)                        
# node3=Node(30)                        
# node4=Node(40)                        
# node5=Node(50)
# l.head=node1
# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=node5
# result=l.display()
# print(result)                        

#find largest number using function
# def maximum(num):
#     largest=num[0]
#     for i in range(len(num)):
#         if num[i]>largest:
#             largest=num[i]
#     return largest
# num=[64,4485,495,9585,949]
# result=maximum(num)
# print(result)    

#find smallest number using function
# def minimum(num):
#     smallest=num[0]
#     for i in range(len(num)):
#         if num[i]<smallest:
#             smallest=num[i]
#     return smallest
# num=[3647,4847,34948,3948]
# result=minimum(num)
# print(result)            

# num=[192,393,3939,39]
# num.append(0)
# print(num)
# num=[93,49,84,746,746,726]
# num.insert(0,10)
# print(num)

#example of finding the second largest using function
# def secondlargest(num):
#     largest=num[0]
#     second=num[0]
#     for i in num:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second and i!=largest:
#             second=i
#     return second
# num=[2884,98755,9587,948,948,973]
# result=secondlargest(num)
# print(result)

#example of reversing using function
# def reverse(num):
#     reverse=[]
#     for i in range(len(num)-1,-1,-1):
#         reverse.append(num[i])
#     return reverse
# num=[23,5,6,6,7,7]
# result=reverse(num)
# print(result)

#example of reversing using slicing method
# num=[3884,4948,4948449,8474]
# num=num[::-1]
# print(num)

#example of insert using function   
# def inserting(num,position,value):
#     num.insert(position,value)
#     return num
# num=[6464,4847,4874,47]
# result=inserting(num,0,1000)
# print(result)    

#example of inserting manually withput using function
# num=[384,585,58575,5857]
# position=0
# value=1000
# num.append(0)
# for i in range(len(num)-1,position,-1):
#     num[i]=num[i-1]
# num[position]=value
# print(num)    

#exxample of deleting an element using function
# def deletion(num):
#     position=3
#     for i in range(position,len(num)-1):
#         num[i]=num[i+1]
#     num.pop()
#      return num
# num=[384,49858,5986,66]
# result=deletion(num)
# print(result)

#example of deletion manually without using function
# num=[2883,984,484]
# position=1
# for i in range(position,len(num)-1):
#     num[i]=num[i+1]
# num.pop()
# print(num)

#example of searching an element using function
# def searching(num):
#     target=3884
#     for i in range(len(num)):
#         if num[i]==target:
#             print("the element is found at index:",i)
#             break
#     else:
#         print("the element is not found")
#     return num
# num=[3884,49483,94874]
# searching(num)

#example of searching an element using function
# num=[39734,874484,94774,8474]
# target=8474
# for i in range(len(num)):
#     if num[i]==target:
#         print("the element is found at index:",i)
#         break
# else:
#     print("the element is not found")

#example of reversing a list manually
# num=[8485,5886,5885]
# start=0
# end=len(num)-1
# while start<end:
#     num[start],num[end]=num[end],num[start]
#     start+=1
#     end-=1
# print(num)

#singly linkedlist entire operations
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
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newnode  
#     def insert_position(self,data,position):
#         newnode=Node(data)
#         if position==0:
#             newnode.next=self.head
#             self.head=newnode
#         else:
#             current=self.head
#             for i in range(position-1):
#                 current=current.next
#             newnode.next=current.next
#             current.next=newnode  
#     def delete_first(self):
#         if self.head is None:
#             return
#         if self.head.next is not None:
#             self.head=self.head.next     
#     def delete_end(self):
#         if self.head is None:
#             return
#         if self.head is None:
#             self.head=None
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next            
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
# l.insert_position(100,4)
# l.delete_first()
# l.delete_end()
# l.delete_position(2)
# l.display()                 

#doubly linked list entire operations
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
#         newnode=Node(data)
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         newnode.prev=current
#         newnode.next=current.next
#         current.next.prev=newnode
#         current.next=newnode   
#     def delete_first(self):
#         self.head=self.head.next
#         self.head.prev=None  
#     def delete_end(self):
#         current=self.head
#         while current.next:
#             current=current.next
#         current.next=None   
#         current.prev.next=None  
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next
#         if self.head is None:
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
# l.insert_first(40)   
# l.insert_end(50)                  
# l.insert_end(60)                  
# l.insert_end(70)                  
# l.insert_end(80)  
# l.insert_position(100,2)  
# l.delete_first()     
# l.delete_end()   
# l.delete_position(2)      
# l.display()

#convert list to linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def convert(self,number):
#         for i in number:
#             newnode=Node(i)
#             if self.head is None:
#                 self.head=newnode
#             else:
#                 current=self.head
#                 while current.next:
#                     current=current.next
#                 current.next=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")    
# num=[2983,984,4984]
# l=Linkedlist()
# l.convert(num) 
# l.display()                 

#convert linkedloist to list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def convert(self):
#         current=self.head
#         num=[]
#         while current:
#             num.append(current.data)
#             current=current.next
#         return num
# l=Linkedlist()
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# l.head=n1
# n1.next=n2
# n2.next=n3
# print(l.convert())         

#stack operations
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         self.stack.pop()
#     def peek(self):
#         print("the top element is:",self.stack[-1])
#     def display(self):
#         print(self.stack)
# s=Stack()
# s.push(10)               
# s.push(20)               
# s.push(30)               
# s.push(40)               
# s.push(50)
# s.pop()
# s.peek()
# s.display()               

#collections.deque operations
# from collections import deque
# d=deque([10,20,30,40,50])
# d.append(60)
# d.appendleft(5)
# d.pop()
# d.popleft()
# print(d[0])
# print(d.maxlen)
# print(d)

#queue operations
# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,data):
#         self.queue.append(data)    
#     def dequeue(self):
#         self.queue.pop()
#     def peek(self):
#         print("top element:",self.queue[0])
#     def display(self):
#         print(self.queue)
# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.dequeue()
# q.peek()
# q.display()

#example of binary search
# num=[10,20,30,40,50]
# target=200
# low=0
# high=len(num)-1
# while low<=high:
#     mid=(low+high)//2
#     if num[mid]==target:
#         print("the element is found at index:",mid)
#         break
#     elif num[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# else:
#     print("the element is not found")        

#example of bubble sort
# num=[293,984,938,9838,3243,72655217,9]
# n=len(num)
# for i in range(n):
#     for j in range(n-i-1):
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]
# print(num)

#example of selection sort
# num=[2093,83664,754,654]
# n=len(num)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if num[j]<num[min_index]:
#             min_index=j
#     num[i],num[min_index]=num[min_index],num[i]
# print(num)         

#example of insertion sort
# num=[1039,984,43,4,5,6]
# n=len(num)
# for i in range(n):
#     key=num[i]
#     j=i-1
#     while j>=0 and num[j]>key:
#         num[j+1]=num[j]
#         j-=1
#     num[j+1]=key    
# print(num)        

#example of counting frequency
# num=[10,20,20,30,30,40,50,50]
# frequency={}
# for i in num:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(frequency)

#example of frequency using function
# def frequent(num):
#     frequency={}
#     for i in num:
#         if i in frequency:
#             frequency[i]+=1
#         else:
#             frequency[i]=1
#     return frequency
# num=[10,20,30,10,20,30]
# result=frequent(num)
# print(result)         

#example of hash function
# data={
#     "name":"ridha",
#     "age":17,
#     "course":"bca"
# }
# print(data["name"])
# del data["age"]

# if "age" in data:
#     print("age exists")
# else:
#     print("age nt exists")
# print(data)

#example of hashcollision
# def hash(key):
#     return key%10
# a=200
# b=35
# hash1=hash(a)
# hash2=hash(b)
# if hash1==hash2:
#     print("hash collision")
# else:
#     print("no collision")

#reverse linkedlist
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
#     def reverse(self):
#         previous=None
#         current=self.head
#         while current:
#             nextnode=current.next
#             current.next=previous
#             previous=current
#             current=nextnode
#         self.head=previous
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")    
# l=Linkedlist()
# l.insert_end(10)            
# l.insert_end(20)            
# l.insert_end(30)            
# l.insert_end(40) 
# l.insert_end(50)
# l.display()
# l.reverse()
# l.display()           

#example of factorial using recursion
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5)) 

#example of dfibanocci using recursion
# def fibanocci(n):
#     if n<=1:
#         return n
#     return fibanocci(n-1)+fibanocci(n-2)
# print(fibanocci(7))

#example of reverse  using recursion
# def reversing(n):
#     if len(n)==0:
#         return n
#     return reversing(n[1:])+n[0]
# print(reversing("ridha fathima"))

#example of removing duplicates using function
# def duplicate(num):
#     unique=[]
#     for i in num:
#         if i  not in unique:
#             unique.append(i)
#     return unique
# num=[10,20,30,40,50,60,60]
# result=duplicate(num)
# print(result)        

#example of two sum in array
# nums=[7,2,5,6,7]
# target=9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])
            

#convert list to linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def convert(self,number):
#         for i in number:
#             newnode=Node(i)
#             if self.head is None:
#                 self.head=newnode
#             else:
#                 current=self.head
#                 while current.next:
#                     current=current.next
#                 current.next=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")
# num=[10,20,30,40,50]
# l=Linkedlist()
# l.convert(num)
# l.display()                                    

#convert linkedlist to list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None  
#     def convert(self):
#         num=[]
#         current=self.head
#         while current:
#             num.append(current.data)
#             current=current.next
#         return num
# l=Linkedlist()
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# l.head=n1
# n1.next=n2
# n2.next=n3
# print(l.convert())
                
#reverse linkedlist
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
#     def reverse(self):
#         current=self.head
#         previous=None
#         while current:
#             nextnode=current.next
#             current.next=previous
#             previous=current
#             current=nextnode
#         self.head=previous
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")    
# l=Linkedlist()
# l.insert_end(10)                                            
# l.insert_end(20)                                            
# l.insert_end(30)                                            
# l.insert_end(40)                                            
# l.reverse()
# l.display()

#example of algorithmic optimisation
# def largest(num):
#     largest=num[0]
#     for i in num:
#         if i>largest:
#             largest=i
#     return largest
# num=[12,4,2,4,5]
# result=largest(num)
# print(result)        

#example of pythonic optimisation
# num=[29878,4984,944]
# print(max(num))

#example of inserting an element
# def inserting(num,position,value):
#     num.insert(position,value)
#     return num
# num=[10,20,30,40]
# result=inserting(num,2,25)
# print(result)

# num=[10,20,30,40,50]
# position=2
# value=25
# num.append(0)
# for i in range(len(num)-1,position,-1):
#     num[i]=num[i-1]
# num[position]=value
# print(num)

# example of deleting an element
# def deleting(num,value):
#     if value in num:
#         num.remove(value)
#     else:
#         print("element is not found")
# num=[10,20,30,40]
# deleting(num,20)
# print(num)         

# num=[102,394,494,49]
# position=3
# for i in range(position,len(num)-1):
#     num[i]=num[i+1]
# num.pop()
# print(num)

#example of searching an element in a list
# def searching(num):
#     target=95
#     for i in range(len(num)):
#        if num[i]==target:
#            print("the element is found",i)
#            break
#     else:
#         print("the element is not found")
#     return num
# num=[2094,404,95]
# searching(num) 

#example of reversing a string
# num=[948,5985,94875,8485]
# start=0
# end=len(num)-1
# while start<end:
#     num[start],num[end]=num[end],num[start]
#     start+=1
#     end-=1
# print(num)

#singly linked list operaions
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkeldist:
#     def __init__(self):
#         self.head=None
#     def insert_first(self,data):
#         newnode=Node(data)
#         newnode.next=self.head
#         self.head=newnode
#     def insert_end(self,data):
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
#     def deletefirst(self):
#         if self.head is None:
#             return
#         if self.head is not None:
#             self.head=self.head.next 
#     def delete_end(self):
#         if self.head is None:
#             self.head=None
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#     def delete_position(self,position):
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkeldist()
# l.insert_first(40)
# l.insert_first(30)
# l.insert_first(20)
# l.insert_first(10)
# l.insert_end(50)
# l.insert_end(60)
# l.insert_end(70)
# l.insert_end(80) 
# l.insert_position(100,2)
# l.deletefirst()
# l.delete_end()
# l.delete_position(3)      
# l.display()             

# #example of doubly linkedlist entire operations
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
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         newnode.next=current.next
#         newnode.prev=current
#         current.next=newnode
#         current.next.pev=newnode
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
#         if self.head is None:
#             current.prev.next=current              
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# l=Linkedlist()
# l.insert_first(40)
# l.insert_first(30)
# l.insert_first(20)
# l.insert_first(10)
# l.insert_end(50)
# l.insert_end(60)
# l.insert_end(70)
# l.insert_end(80)
# l.insert_position(100,3)     
# l.delete_first()
# l.delete_end()
# l.delete_position(3)
# l.display()       

#example of converting list to linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def convert(self,num):
#         for i in num:
#             newnode=Node(i)
#             if self.head is None:
#                 self.head=newnode
#             else:
#                 current=self.head
#                 while current.next:
#                     current=current.next
#                 current.next=newnode
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")
# num=[10,20,30,40]
# l=Linkedlist()
# l.convert(num)
# l.display()

#example of converting linkedlist to list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def convert(self):
#         current=self.head
#         num=[]
#         while current:
#             num.append(current.data)
#             current=current.next
#         return num     

# l=Linkedlist()
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# l.head=n1
# n1.next=n2
# n2.next=n3
# print(l.convert())                             

#example reverse linkedlist
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
#     def reverse(self):
#         current=self.head
#         previous=None
#         while current:
#             nextnode=current.next
#             current.next=previous
#             previous=current
#             current=nextnode
#         self.head=previous
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("none")    
# l=Linkedlist()                        
# l.insert_end(10)
# l.insert_end(20)
# l.insert_end(30)
# l.insert_end(40)
# l.reverse()
# l.display()

#example of stack operation
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         self.stack.pop()
#     def peek(self):
#         print("top element:",self.stack[-1])
#     def display(self):
#         print(self.stack)
# s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)

# s.peek()
# s.pop()
# s.display()

#example of queue operations
# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,data):
#         self.queue.append(data)
#     def dequeue(self):
#         self.queue.pop(0)
#     def peek(self):
#         print("top element:",self.queue[0])
#     def display(self):
#         print(self.queue)
# q=Queue()
# q.enqueue(10)                      
# q.enqueue(20)                      
# q.enqueue(30)                      
# q.enqueue(40)
# q.dequeue()
# q.peek()
# q.display()                      

#using collections.deque in stack
# from collections import deque
# stack=deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print(stack)
# stack.appendleft(5)
# stack.popleft()
# stack.pop()
# print(stack)

#example of linear search
# num=[10,87,65,54,52,74]
# target=54
# for i in range(len(num)):
#     if num[i]==target:
#         print("the element is found at index:",i)
#         break
# else:
#     print("the element is not found")    

#example of binary search
# num=[10,20,30,40,50]
# target=40
# low=0
# high=len(num)-1
# while low<=high:
#     mid=(low+high)//2
#     if num[mid]==target:
#         print("the element is found at index:",mid)
#         break
#     elif num[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# else:
#     print("the element is not found")         

#example of bubble sort
# num=[10,20,76,67,89,98]
# n=len(num)
# for i in range(n):
#     for j in range(n-i-1):
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]
# print(num)            

#example of selection sort
# num=[45,87,32,34,65]
# n=len(num)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if num[j]<num[min_index]:
#             min_index=j
#
#     num[i],num[min_index]=num[min_index],num[i]
# print(num)       

#example of insertion sort
# num=[34,32,21,12,3,4]
# n=len(num)
# for i in range(n):
#     key=num[i]
#     j=i-1
#     while j>=0 and num[j]>key:
#         num[j+1]=num[j]
#         j-=1
#     num[j+1]=key
# print(num)    

#example of .sort method
# num=[65,7,8,7,5]
# num.sort()
# print(num)

#example of sorted method
# num=[39894,4939,3834]
# nums=sorted(num)
# print(nums)
# print(num)

#example of hash
# data={
#         "name":"ridha",
#         "age":17,
#         "course":"bca"
# }
# print(data["name"])
# if "age" in data:
#     print("age exists")
# del data["course"]
# print(data)


#example of hash collision
# def hashing(key):
#     return key%10
# a=35
# b=25
# hash1=hashing(a)
# hash2=hashing(b)
# if hash1==hash2:
#     print("hash collision")
# else:
#     print("no collision")

#example of frequency counting
# num=[10,10,20,30,40,50,50,50]
# frequency={}
# for i in num:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(frequency)        