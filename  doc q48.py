# Q48.Write a Python program to find the length of a given dictionary values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:

d={1: 'red', 2: 'en', 3: 'priya', 4: 'whit', 5: 'ack'}
j={}
for i in d:
    a=(len(d[i]))
    j.update({a:d[i]})
print(j)
