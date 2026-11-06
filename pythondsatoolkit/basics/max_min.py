#get maximum and minimum number from an array
# def find_max_min(numbers):
#     maximum = numbers[0]
#     minimum = numbers[0]

#     for i in numbers:
#         if i > maximum:
#             maximum = i

#         if i < minimum:
#             minimum = i

#     return maximum, minimum


# numbers = [10, 5, 30, 2, 50]

# maximum, minimum = find_max_min(numbers)

# print("Maximum:", maximum)
# print("Minimum:", minimum)

#compare list.append vs list.insert(0,x)

# numbers = [10, 20, 30, 40, 50]

# Using append()
# numbers.append(60)
# print("After append:", numbers)

# # Using insert()
# numbers.insert(0, 5)
# print("After insert:", numbers)


 #time complexity of find max function
# def find_max(numbers):
#     maximum = numbers[0]

#     for i in numbers:
#         if i > maximum:
#             maximum = i

#     return maximum


# numbers = [10, 5, 30, 2, 50]

# print("Maximum:", find_max(numbers))

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
