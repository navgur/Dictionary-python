d=["a","b","y","f","rani"]
for i in  range ((len(d))):
    for j in range ((len(d))):
        if d[i]<d[j]:
            tem=d[i]
            d[i]=d[j]
            d[j]=tem
print(d)