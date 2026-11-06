#converting python list to linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
numbers=[1,2,3,4,5,7]
head=None
tail=None
for num in numbers:
    newnode=Node(num)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
current=head
while current:
    print(current.data)
    current=current.next        
