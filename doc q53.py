# Q53.
# Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
# 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5:
# ['Zachary Simon', 'VII']}

k=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,'Zachary Simon', 'VII']]
h={}
w=[]
for i in k:
    for j in i:
        print(j)
        

# # for i 

# a={"name":"prachi","age":20,"college":"uti","graudation":"pass  "}
# d={}
# f=a["name"]
# for i in a:
#     if a[i]!=f:
#         d.update({i:a[i]})
# print(d)

# class dictObj(object):
#      def __init__(self):
#          self.x = 'red'
#          self.y = 'Yellow'
#          self.z = 'Green'
#      def do_nothing(self):
#          pass
# test = dictObj()
# print(test.__dict__)