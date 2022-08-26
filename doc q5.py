# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# e={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# y=[]

# for i in e:
    # y.append(e[i])
    # for i in range (y):
    #     for j in range (y):

t= {3:"a",4:"d",7:"f",2:"b"}
li=[]
e={}
for i in t:
    li.append(n)
for b in range (len(li)):
    for j in range (len(li)):
        if li[b]>li[j]:
            li[b],li[j]=li[j],li[b]
print(li)
for h in li:
    for k in t:
        if k==h:
            print(t[k])
#             e.update({k:t[k]})
# print(e)

# l=[2,4,5,[5,6,7],7,4,[3,5,6]]
# h=[]
# i=0
# while i<len(l):
#     if type(l[i])==list:
#        j=0
#        while j<len(l[i]):
#             h.append(l[i][j])
#             j=j+1
#     else:
#         h.append(l[i])
#     print(h)
# i=i+1


