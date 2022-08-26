# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary: {'S 001': ['Math', 'Science'], 'S
# 002': ['Math',
# 'English']}
# New dictionary: {'S001': ['Math', 'Science'], 'S002': ['Math',
# 'English']}


f={'S 001': ['Math', 'Science'], 'S  002': ['Math','English']}
g={}
k=[]
for d in f:
    # print(f[d])

    k.append(d)
    for i in range(len(k)):
           sum=" "
           for j in range(len(k[i])):
               if k[i][j]!=" ":
                   sum=sum+k[i][j]
    g.update({sum:f[d]})
print(g)
    