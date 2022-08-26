m = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=m
i=0
while i<len(m):
    j=0
    while j<len(m[i][j]):
        if m[i][j]>max:
            max=m[i][j]
        j=j+1
    i=i+1
print(max)        
# x = m.values()
# maximum =max(x)
# print(maximum)
