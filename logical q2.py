# d={"a":"radha","b":"rani"}
# b={"a":"rani","c":12}
# for i in d:
#     if  i in b:
#         d[i]=d[i]+b[i]
#     else: 
#         d[i]=d[i]
# for j in b:
#     if j in d:
#         d[j]=b[j]+d[j]
#     else:
#         d[j]=b[j]
# print(d)

# l=["10100","01001","1002"]
# i=0
# f=[]
# while i<len(l):
#     j=0
#     sum=""
#     while j<len(l[i]):
#         if l[i][j]!="0":
#             sum=sum+(l[i][j])
#         j=j+1
#     f.append(sum)
#     i=i+1
# print(f)

# l=[5,0,3,0,0,1,0,2,4]
# i=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
#         j=j+1
#     i=i+1
# print(l)

# t = {3:"a",4:"d",7:"f",2:"b",6:"t"}
# m=[]
# li=[]
# e={}
# n=[]
# for i in t:
#     li.append(t[i])
# for i in range (len(li)):
#     for j in range (len(li)):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
# for k in range (len(li)):
#     if k==5:
#         break
#     f=li[k]
#     n.append(f)
# for i in n:
#     for j in t:
#         if i==t[j]:
#             e.update({j:i})
# print(e)






# print(li)
# for h in li:
#     for k in t:
#         if h==t[k]:
#             e.update({k:h})
# print(e)


# dic={1:{5:"m"},2:{4:"n",6:{0:"o"}}}
# for i in dic:
#     print(dic([6][i]))
# g={}
# for x,y in dic.items():
#     for i in y:
#         if type(y[i])==dict:
#             a=y[i]
#             for i in a:
#                 print(a[i])


#         for j in y[i]:
#             a=j
#             if a=="O":
#                 g.update({x:a})
# print(g)

a={4:"priya",8:{3:"5",9:"w"}}
for i in a:
    if type(a[i])==dict:
         print(a[i][9])