# Q17.Write a Python program to sort a dictionary by key.
dic1={"a":4,"g":6,"k":8,"c":5}
u=[]
y={}
for i in dic1:
    u.append(i)
    for t in range (len(u)):
        for j in range (len(u)):
            if u[t]<u[j]:
                u[t],u[j]=u[j],u[t]
for h in u:
    for e in dic1:
        if e==h:
            y.update({h:dic1[e]})
print(y)



