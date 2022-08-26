# Q36.Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict= {'key1':1, 'key2':3, 'key3':2}
dict1={'key1':1, 'key2':2}
g={}
for i in dict:
    for j in dict1:
        if dict[i]==dict1[j] and i==j:
            print({j:dict[j]},"is present in both x and y")
            
print(g)
            