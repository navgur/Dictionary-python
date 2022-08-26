t={'V': [1, 3,8,2, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
f={}
for i in t:
    h=[]
    for j in t[i]:
        if j%2==0:
            h.append(j)
    f.update({i:h})

print(f)
