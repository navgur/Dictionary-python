l=["rani","priya","teena"]
a=["singh",12,"chauhan",56,"tiwari",34]
h={}
z={}
s={}
for i in range (len(l)):
    w=[]
    for j in range (len(a)):
        if type(a[j])==str:
            z.update({"surname":a[j]})
        w.append(z)
    else:
        s.update({"age":a[j]})
        w.append(s)
        print(w)



    


