# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
# dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5
dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
u=[]
for t in dict:
    u.append(t)
for i in range (len(t)):
    c=0
    for j in range (len(t)):    
            c=c+1
print(c)
