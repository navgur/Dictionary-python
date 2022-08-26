# dict1={"brand":"suzuki","model":"Dzire","year":2020}
# x=dict1["model"]
# print(x)

# print(dict1)
# x=dict1["model"]
# print(x)
# y=dict1.get("model")
# print(y)

# Accessing Items


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # x = thisdict["model"]
# # print(x)
# # here is also a method called get() that will give you the same result:
# x = thisdict.keys() 
# print(x)


# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

x=car.key()
print(x)
car["model"]="white"
print(x)