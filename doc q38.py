# Q38.. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

y={'c1': 'Red', 'c2': 'Green', 'c3': None}
t={}
for i in y:
    if None !=y[i]:
        t.update({i:y[i]})
print(t)
            