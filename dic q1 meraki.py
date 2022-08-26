dict1={1:10, 2:20}
dict2={3:30,2:40}
dict3={5:50,3:60}
h={}
for i in dict2:
        if i in dict1:
            dict1[i]=dict1[i]+dict2[i]
        else:
           dict1[i]=dict2[i]
        dict1.update(dict3)
print(dict1)
            

# for i in d1:
#     if i in d2:
#         d[i]=d1[i]+d2[i]
#     else:
#         d[i]=d1[i]
# for j in d2:
#     if j in d1:
#         d[j]=d1[j]+d2[j]
#     else:


#         d[j]=d2[j]

# print(d)        
