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
# l.display()                            