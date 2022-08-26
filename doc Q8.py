# Write a Python program to check whether a given key already exists in a dictionary.
from re import I


dic1={"name":45,"meena":46,"youth":23}
# key=input("enter the number")
# # for i in dic1:
# if key in dic1:
#     print("exist")
# else:
#     print("not exist")
# # break

# # for i in dic1:
# if "name"in dic1:
#     print("exist")
# else:
#     print("not exist")
# for i in dic1:
#     print(i)
# f=dic1["name"]
# h={} 
# for i in dic1:
#     if dic1[i]!=f:
#         h.update({i:dic1[i]})
# print(h)

# l=[]
# for t in dic1:
#     l.append(dic1[t])
#     for i in range (len(l)):
#         for j in range (len(l)):
#             if l[i]<l[j]:
#                 l[i],l[j]=l[j],l[i]
# print(l)
        

# rWrite a Python program to remove duplicates from Dictionary.
data = {'id1':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id2':
{'name': ['David'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id4':{'name': ['Surya'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
}
g={}

y=data["id1"]
for i in data:
     
