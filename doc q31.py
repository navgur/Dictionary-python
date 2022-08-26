# Q31.. Write a Python program to get the top three items in a shop. Go to
# the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
# 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


h= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
 'item5': 24}
max=0
max1=0
max2=0
a=""
b=""
c=""
for x,y in h.items():
    if y>max:
        max=y
        a=x
    if y>max1 and y!=max:
         max1=y
         b=x
    if y>max2 and y!=max and y!=max1:
        max2=y
        c=x

        print(a,max)
        print(b,max1)
        print(c,max2)
