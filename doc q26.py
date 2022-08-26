# Q26.
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Sample Output:
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 1

dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
j=[]
for i in dic:
    print(i,end=" ")
    if type(dic[i])==list:
        # a=dic[i]
        j.append(dic[i])

print()
for i in range(len(j)):
    for t in range(len(j[i])):
        w=j[t][i]
        print(w,end="  ")
    print()

        
        



# for s in dic:
#     print(s,end=" ")
# print()
# h=list(dic.values())
# # print(h)
# for i in range(len(h)):
#     for j in range (len(h)):
#         t=h[j][i]
#         print(t,end="  ")
#     print()
# # print(t)