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