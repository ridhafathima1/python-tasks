#converting python list to linked list
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

#converting linkedlist into python list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4
head=node1
numbers=[]
current=head
while current:
    numbers.append(current.data)
    current=current.next

print(numbers)