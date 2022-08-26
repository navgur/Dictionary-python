
# Write a Python program to combine values in python list of dictionaries.
#  data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
# 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})}
data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1','amount': 750}]
r={}  
for i in data:
     key=i["item"]
     value=i["amount"]
if key not in r. keys(): 
     t={key:value}
     r.update(t)
else:
     r[key]+=value
print(r)    

