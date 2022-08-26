# a={"ankita":10,"anjali":20,"rani":30}
# e=[]
# j=[]
# for i in a:
#     e.append(i)
#     j.append(a[i])
# print(e,j)


# l=["rani","ankita","shweta","anjali.s"]
# k={}
# for i in range (len(l)):
#     a=len(l[i])
#     k.update({l[i]:a})
# print(k)


# a=[1,2,8,[4,5,6,[7,8,9,1],7]]
# sum=0
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         n=0
#         while n<len(a[i]):
#             if type(a[i][n])==list:
#                 d=0
#                 while d<len(a[i][n]):
#                     sum=sum+a[i][n][d]
#                     d=d+1
#             else:
#                 sum=sum+a[i][n]
#             n=n+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)

    

    #         h=0
    #         while h<len(b):
    #             sum=sum+b[h]
    #         print(sum)
    #         j=j+1
    # i=i+1


#                 f=0
#                 while f<len(k):
#                     sum=sum+f
#                 f=f+1
#                 print(sum)

#             else:
#                 t=a[i][j]
#             j=j+1
#     i=i+1
# print(k)

# #                 m=0
# #                 while m<len(k):print(k[m])

# #                 # v=a[i][j]
# #     #             print(v)
# #     #         else:
# #     #             c=a[i]
# #         j=j+1
# #     i=i+1
# # print(k[m]

l={'a':5,'b':[5,7,9],'c':[7,9,8]}
t={}
for i in l:
    if (type(l[i]))==list:
        sum=0
        for h in range (len(l[i])):
            sum=sum+l[i][h]
            t.update({i:sum})
    else:
        t.update({i:l[i]})
print(t)


# h={}
# for t in l:
#     if type(l[t])==list:
#         sum=0
#         for k in range(len(l[t])):
#             sum=sum+l[t][k]
#         h.update({t:sum})
#     else:
#         h.update({t:l[t]})
# print(h)
        
# dic={"one":12,"two":4,"three":67,"four":34,"five":23}
# j=[]
# g=[]
# y=[]
# for i in dic:
#     if dic[i]%2==0:
#         j.append(dic[i])
#     else:
#         g.append(dic[i])
# y.append(j)
# y.append(g)
# print(y)

dic={{"a":4,"b":9},{"n":6,"m":4}, "r":6 ,{"r":78,"t":12},"j":77,"h":5}
for i in range (len(dic)):
    if type (dic[i])==dict:
        sum=0
        for t in dic[i]:
            sum=sum+dic[i][t]
        print(sum)
    

    for j in i:
        print(j)





