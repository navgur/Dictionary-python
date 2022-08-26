# Q21.Write a Python program to print all unique values in a dictionary.
data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
 {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}





# data = {{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}}
# for i in data:
#     print(i)
u=[]
for i in data:
    for g in i:
        if i[g]not in u:
            u.append(i[g])
print(set(u))

# h={2:"t",3:"rt"}
# t={}
# if len(h)==0:
#         print("empty")
# else:
#     print("not empty")

