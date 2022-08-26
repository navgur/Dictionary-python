# Q23.Write a Python program to find the highest 3 values of corresponding keys in a
# dictionary.

# dic1={"rani":5000000, "ybuhi":4386767000, "teena":23000, "rohi":8}
# max=dic1["rani"]
# max1=dic1["rani"]
# max2=dic1["rani"]
# for i in dic1: 
#     for j in dic1:
#         if max<dic1[j]:
#            max=dic1[j]
#         if max1<dic1[j] and max!=dic1[j]:
#             max1=dic1[j]
#         if max2<dic1[j] and max!=dic1[j] and max1!=dic1[j]:
#             max2=dic1[j]
# print(max)
# print(max1)
# print(max2)
    


           


d = {"a":500, 'b':587, 'c': 560,'d':400, 'e':5874, 'f': 20,"t":5000,"r":10000}
max1=d["a"]
max2=d["a"]
max3=d["a"]
for i in d:
    for j in d:
        if max1<d[j]:
            max1=(d[j])
        if max2<d[j] and max1!=d[j]:
            max2=d[j]
        if max3<d[j] and max1!=d[j] and max2!=d[j]:
            max3=d[j]
print(max1)
print(max2)
print(max3)