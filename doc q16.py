# Q16.Write a Python program to map two lists into a dictionary.

# l1=[1,3,9]
# l2=["anjali","rani","pooja"]
# h={}
# for i in range (len(l1)):
#     h.update({l1[i]:l2[i]})
# print(h)
dic1={"rani":4,"ui":877,"priya":8,"teena":78,"yes":-3}
max=dic1["rani"]
min=dic1["rani"]
for i in dic1:
    if dic1[i]>max:
        max=dic1[i]
    if dic1[i]<min:
        min=dic1[i]
print(max)
print(min)
