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

