# Q22. Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bcbd


data ={'1':['a','b'], '2':['c','d']}
g=data["1"]
h=data["2"]
for i in g:
    for j in h:
       print(i+j)
