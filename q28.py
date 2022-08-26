# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}



li=[1,2,3,4]                                                                                      
h={}
for i in range (1,(len(li)+1)):
    h=({li[-i]:h})
print(h)

# l=[1,2,3,4,[6,4,5,3],1,2]
# i=0
# summ=0
# while i<len(l):
#     if type(l[i])==list:
#         k=0
#         sum=0
#         while k<len(l[i]):
#          sum=sum+l[i][k]
#          summ=summ+l[i][k]
#          k=k+1
#     else:
#         summ=summ+l[i]
    
#     i=i+1
# print(sum)
# print(summ)

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# while a<=b:
#     i=1
#     while i<=10:
#         print(a,"*",i,"=",a*i)
#         i=i+1
#     print()
#     a=a+1

# for i in range(1,11):
#     while i<=100:
#         print(i,end=" ")
#         i=i+10
#     print()

# a=int(input("enter the number"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i=i+1

# num=int(input("enter the number"))
# i=1
# while i<=num:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     print()
#     i=i+1

# num=int(input("enter the number"))
# k=[]
# i=1
# while i<=num:
#     name=input("enter the name")
#     k.append(name)
#     i=i+1
# print(k)

# w=int(input("enter the number"))
# a=[1,2,3,4,5,6,7,8,9,10,45,78,25,36,88]
# e=[]
# i=0
# c=0
# while i<len(a):
#     if i%2!=0:
#         c=c+1
#         d=w*c
#         e.append(d)
#     else:
#         e.append(a[i])
#     i=i+1
# print(e)

# num=int(input("enter the number"))
# fac=1
# while num>0:
#     fac=fac*num
#     num=num-1
# print("factorial=",fac)