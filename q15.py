dic1={5:"yuhi",7:"teena",98:"rani"}
g=dic1[5]
t={}
for i in dic1:
    if dic1[i]!=g:
        t.update({i:dic1[i]})
print(t)


# v=dic1.popitem()
# print(dic1)