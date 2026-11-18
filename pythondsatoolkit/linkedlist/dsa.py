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
       