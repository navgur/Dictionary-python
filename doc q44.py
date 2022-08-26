# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# # {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]

# r={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# k=[]
# for i in r:
#     h={}
#     if i=="science":
#         for j in r[0]:
#             print(r[0][j])

            
        






    # for x,y in r.items():
    #     for t in y:
    #         for e in ((t[y])) :
    #             print(e)

# from re import I


# r=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color':
# 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color':
# 'Olive'}]
# d={}
# for i in range  (len(r)) :
#     if r[0] !=r[i]:
#         d.update({i:r[i]})
# print(d)

# a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# s=[]
# h={}
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
# for i in range (len(a)):
#     h.update({i:int a[i]})
# print(h)


r=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# f={}
# for i in r:
#     if i[0] not in f.keys():
#         f.update({i[0]:[i[1]]})
#     else:
#         l=f[i[0]]
#         l.append(i[1])
#         f.update({i[0]:l})
# print(f)
# g={}
# for i in range(len(r)):
#     for j in range(len(r[i])):
#         if r[i][0]not in g:

# l=[3,5,80,6,7,8,0,3,67]
# max=0
# max2=0
# i=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     if l[i]>max2 and l[i]!=max:
#         max2=l[i]    
#     i=i+1
# print(max2)


t={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
h=[]
for i in  range (0,4):
    g={}
    for r in t:
        for j in t:
            if r==j:
                g.update({j:t[j][i]})
    h.append(g)
print(h)


    
        