
# q6.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
f={0:10,1:20,2:30}
# sum=0
# sum1=0
# for i in f:
#     sum1=sum1+f[i]
#     sum+=i
# print({sum:sum1})
f[6]=8
print(f)
f.update({5:8})
print(f)

