list1=["one","TWO","THREE","FOUR","FIVE"]
list2=[1,2,3,4,5,]
i=0
g={}
while i<len(list1):
    g.update({list1[i]:list2[i]})
    i=i+1
print(g)    
