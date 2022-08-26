a={"course":"python","fees":5000,1:{"course":"javascript","fees":10000}}
for i in a:
    if  type (a[i]) is dict:
       for k in a[i]:
           print(k,"=",a[i][k])
    else:
        print(i,"=",a[i])
        # q2"

# a={1:{"apple":10,"ball":2},2:{"bat":10,"cat":4}}
# for i in a:
    
#     if  type (a[i])==dict:
        
#          for j in a[i]:
#             print( i,j,"=",a[i][j])
    
# dic={"1":{"neha":"10","sejazl":"12"},"2":{"jai":"19","anjali":"15"}}
# for i in dic:
#     if type (dic[i])==dict:
#         for n in dic[i]:
#             print(i, n,dic[i][n])
        
    
        