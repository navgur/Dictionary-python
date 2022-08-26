# di={"ram":"raj","2":22,"teena":6}
# d=di["ram"]
# n={}
# for i in di:
#     if d != di[i]:
#         n.update(({i:di[i]}))
#         n.update({"arti":"raj"})
# print(n)



# a=di.pop("ram")
# di.update({"arti":"raj"})
# print(di) 

# i=0
# while i<10:
#     i=i+1
#     if i%2==0:
#         pass
#     if i==5:
#         continue
#     if i%2!=0:
#         print(i,"odd")
#     if i==7:
#         break



#     # if i==5:
#     #     continue
#     # elif i==6:
#     #     pass
#     # if i==7:
#     #     break
#     # print(i) 
num=int(input("enter the number"))
i=1
sum=0
while i<=10:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print("perfect")
else:
    print("not")
        