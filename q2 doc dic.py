string="W3resource"
d={}
# for i in string:
#     if i not in d:
#         d[i]=0
#     d[i]+=1
# print(d)
for i in range(len(string)):
    c=0
    for j in range(len(string)):
        if string[i]==string[j]:
            c=c+1
            d.update({string[i]:c})
            print(d)            
