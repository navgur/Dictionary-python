# a="w3resource"
# h={}
# # for i in a:
# #     if  i not in h:
# #         h[i]=0
# #     h[i]+=1
# # print(h)
# for i in range  (len(a)):
#     c=0
#     for j in range (len(a)):
#         if a[i]==a[j]:
#             c=c+1
#             h.update({a[i]:c})
# print(h)


dic={"a":400,"r":500,"w":200}
dic2={"a":100,"y":70,"w":20}
d={}
for i in dic:
    if i in dic2:
        d[i]=dic[i]+dic2[i]
    else:
        d[i]=dic[i]
for j in dic2:
    if j in  dic:
        d[j]=dic[j]+dic2[j]
    else:
        d[j]=dic2[j]
print(d)


# h={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary''Simon']}
# l={}
# f=[]
# for x,y in h.items():
#     for i in y:
#         l.update({x:i})
# f.append(l)
# print(f)


        

# g=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
# 'Zachary Simon', 'VII']]
# # k={}
# for i in range (len(g)):
#     l=[]
#     for j in range (len(g[i])) :
#         if type(g[i][j])==int:
#             a=(g[i][j])
#         else:
#             l.append(g[i][j])
#             k.update({a:l})
# print(k)


#     if type(g[i][0])==int:
#         a=(g[i][0])
#         k.update({a:g[i]})
# print(k)

# t={'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# h=[]
# for i in t:
#     h.append(i)
#     for i in range (len(i)):
#         for j in range

# dic={1:[3,4,5,6],5:[5,6,7]}
# for i in dic:
#     a=dic[i]
# print(a)

# li=[1,3,4,5]
# y={}
# h={}
# for i in range(1,(len(li)+1)) :
#     k=li[-i]
#     print(k)
#     y=({k:y})

# print(y)
    

# list=[1,2,3,4]                                                                                      
# t=count={}
# for i in list:
#     count[i]={}
#     count=count[i]
# print(t)


# from traceback import format_exception_only


# t=[{'id': 1, 'success': True, 'name': 'Lary'},
# {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]

# y=t["id"]
# print(y)

# dic1={4:7,9:1,9:3}
# if len(dic1)==0:
#     print("empty dic")
# else:
#     print("not")
# data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
# {"V":"S009"},{"VIII":"S007"}]
# h=[]
# for i in range  (len(data)):
#     for j in data[i]:
#         if data[i][j] not in h:
#             h.append(data[i][j])
# print(set(h))
# t={'1':['a','b'], '2':['c','d']}
# r=t["1"]
# k=t["2"]
# for i in r:
#     for j in k:
#         print(i+j)

# from re import I


# from tkinter import Y




d={5:3,7:8,3:6,"b":9,4:3,"teena":45,"c":90,1:1}
o=[]
max=0
# max1=0
# max2=0
# for i in d:
#     for j in d:
#         if d[j]>max:    
#             max=d[j]
#             c=j
#         if d[j]>max1 and d[j]!=max:
#             max1=d[j]
#             v=j
#         if d[j]>max2 and d[j]!=max1 and d[j]!=max:
#             max2=d[j]
#             e=j
# o.append(c)
# o.append(v)
# o.append(e)
# print(o)
# print(max)
# print(max1)
# print(max2)

# data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
# 'amount': 750}]
# w={}
# for i in data:
#     d=i["item"]
#     y=i["amount"]
#     if d not in w:
#         t={d:y}
#         w.update(t)
#     else:
#         w[d]=+y
# print(w)




# dic= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# h=[]
# for t in dic:
#     print(t,end="")
#     if type (dic[t])==list:
#         h.append(dic[t])
# print()
# for i in range(len(h)):
#     sum=0
#     for j in range(len(h[i])):
#         g=h[i][j]
#         print(g,end=" ")
#     print()    

# t = [{'id': 1, 'success': True, 'name': 'Lary'},
# {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]

# for i in range (len(t)):
# sum=0
# for i in range (len(t)):
#     for j in t[i]:
#         # print(t[i][j])
#         if type (t[i][j])==int:
#             sum=sum+t[i][j]
# print(sum)


# list = [1, 2, 3, 4,5]
# h={}
# for i in range (1,(len(list)+1)):
#     h={list[-i]:h}
# print(h)
 
# t= {'S 001': ['Math', 'Science'], 'S0  02': ['Math','English']}
# o=[]
# s={}  
# for u in t:
#     o.append(u)
# for i in range (len(o)):
#     sum=""
#     for j in range (len(o[i])):
#         if o[i][j]!=" ":
#             sum=sum+o[i][j]
#     s.update({sum:t[u]})
# print(s)

# s = {'Aex':{'class':'V',
# 'rolld_id':2},
# 'Puja':{'class':'V',
# 'roll_id':3}}
# for i in s:
#     for j in s[i]:
#         print(j,":",s[i][j])
        
    

# dic = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in dic:
#     if type (dic[i])==list:
#         for t in range (len(dic[i])):
#             c=c+1
# print(c)

# y= {'key1': 1, 'key2': 3, 'key3': 2}
# t={'key1': 1, 'key2': 2}
# for i in y:
#     for j in  t:
#         if y[i]==t[j] and i==j:
#             print({i:y[i]},"is present in both y and t")


# a = {'id1':
# {'name': ['Sara'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# 'id2':
# {'name': ['David'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# 'id3':
# {'name': ['Sara'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# 'id4':{'name': ['Surya'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# }
# for i in a:
#     print(i)
#     for j in a[i]:
#      print({j:a[i][j]})
# g={}
# for i in a:
#     if a[i] not in g.values():
#         g.update({i:a[i]})
# print(g)


# for i in a:
#     if a[i]!=b:
#         g.update({i:a[i]})
# print(g)
    

# g={}

# for x, y in a.items():
#     if y not in g.values():
#         g[x]=y
# print(g)

# r={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i in r:
#     for j in range(len(r[i])):
#         if j==4:
#             print(r[i][j])
# for i in r:
#    print(i,"has value",r[i])

# r={'c1': 'Red', 'c2': 'Green', 'c3': None}
# h={}
# for i in r:
#     if r[i]!=None:
#         h.update({i:r[i]})
# print(h)


# t={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190,"priya":56}
# g={}
# for i in t:
#     if t[i]>170:
#         g.update({i:t[i]})
# print(g)

# g=['S001', 'S002', 'S003', 'S004']
# d=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# e=[85, 98, 89, 92]
# f=[]
# for i in range (len(g)):
#     k={}
#     m={}
#     k.update({d[i]:e[i]})
#     m.update({g[i]:k})
#     f.append(m)
# print(f)

# y=[]
# for i in range (len(g)):
#     h={}
#     m={}
#     h.update({a[i]:t[i]})
#     m.update({g[i]:h})
#     y.append(m)
    
# print(y)

# r={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (6.0, 69), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
# 66)}
# y={}
# for i in r:
#     for j in range (len(r[i])):
#         if r[i][j]>=6 and r[i][j]>=70:
#             y.update({i:r[i]})
# print(y)
    


# e={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 14, 'Pierre Cox': 12}
# value=int(input("enter the number"))
# value=int(input("enter the number"))
# c=0
# for i in e:
#     if e[i]==value:
#         c=c+1
# if c==len(e):
#     print("true")
# else:
#     print("false")

# r=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


# r=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# t={}
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# r=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
# for i in range (len(r)):
#     for j in r[i]:
#         t.update({j:int(r[i][j])})
#     print(t)
# e={}
# k=[]
# for i in range (len(r)):
#     for j in r[i]:
#         e.update({j:float(r[i][j])})
# # print(e)
# k.append(e)
# print(k)

# r={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in r:
#     r[i]=[]
# print(r)
        

# Original Dictionary:
# e={1: 'red', 2: 'green', 3: 'blacke', 4: 'whittte', 5: 'black',6:"four"}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# g={}
# for i in e:
#    a=(len(e[i]))
#    g.update({e[i]:a})
# print(g)



# s={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
# g={}
# m=[]
# for i in s:
#     for j in s[i]:
#         g.update({i:j})
# m.append(g)
# print(m)


# d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# h=[]
# q=[]
# for t in d:
#     h.append(d[t])
#     for i in range (len(h)):
#         for j in range (len(h)):
#             if h[i]>h[j]:
#                 h[i],h[j],=h[j],h[i]
# print(h)

# for o in h:
#     for z in d:
#         if o==d[z]:
#             c=c+1
#             print(z)

#             q.append(z)
# print(q)



# t= {3:"a",4:"d",7:"f",2:"b"}
# li=[]
# e={}
# for i in t:
#     li.append(i)
# for b in range (len(li)):
#     for j in range (len(li)):
#         if li[b]>li[j]:
#             li[b],li[j]=li[j],li[b]
# print(li)
# for h in li:
#     for k in t:
#         if k==h:
#             print(t[k])

r={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}
h=[]
g={}



# a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# # Convert the said dictionary into a list of lists:
# # [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
# # g=[]
# j=[]

# for i in a:
#     if i in a:
#         c=[i,a[i]]
#         j.append(c)
# print(j)

# r={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}
# j={}
# for i in r:
#     a=len(r[i])
#     j.update({r[i]:a})
# print(j)

# e=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# # Grouping a sequence of key-value pairs into a dictionary of lists:
# # {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# k=[]
# l={}
# for i in range (len(e)):
#     l.update({i[0]:[i][1]})
# print(l)
#     a=(e[i][0])
#     for j in range (len(e[i])):
#         # if type(e[i][j])==int:
#             if a in e[i][j]:
#                 k.append(e[i][j])
# print(k)
                
# s=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
# 'Zachary Simon', 'VII']]
# g={}
# for i in s:
#     g.update({i[0]:[i[1],i[2]]})
# print(g)


r={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
h={}
for i in  r:
    g=[]
    for j in r[i]:
        if j%2==0:
            g.append(j)
            h.update({i:g})
        else:
            h.update({i:r[i]})
print(h)