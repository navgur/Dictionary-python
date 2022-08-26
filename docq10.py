# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are square of keys.
# dic1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196
# 15: 225}
# dic1={5:6,6:9,3:6,8:9}
# d={}
# # for i in dic1:
# #     a=i*i
# #     d.update({a:dic1[i]})
# # print(d)
# for i in dic1:
#     a=i*i
#     b=dic1[i]*dic1[i]
#     d.update({a:b})
# print(d)
# g={}
# for i in range(1,16):
#     g.update({i:i*i})
# print(g)



# a=[1,2,[3,8,4,[6,9,2],8,[0],3,[29,3,8],3,8,2],3,9,6]
# # o/p:-[1,2,3,8,4,6,9,2,8,0,3,29,3,8,3,8,2,3,9,6]
# i=0
# h=[]
# while i<len(a):
#     if type(a[i])==list:
#         b=a[i][j]
#         while b<len(a[i]):
#            h.append(a[i][j])
#     else:
#        h.append(a[i])
#        j=j+1
#     i=i+1
# print(h)

        