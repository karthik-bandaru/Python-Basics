# input = ['apple':2,'banana':1,'cherry':3]
#output = ['banana':1,'apple':2,'cherry':3]
# a = {'apple':2,'banana':1,'cherry':3}
# a.values()
# print(a)
# print(a['apple'])
# L = []

# for i in range(len(a)):               ## This Wrong We cant get the a[1] in dict
#     min = i                           ## We have to use key for the value...
#     for j in range(i+1,len(a)):
#         if a[j] < a[min]:
#             min = j              
#     a[i],a[min] = a[min],a[i]
# print(a)

# for i,j in a.items():
    # L.append(tuple(i,j))

# print(L)    

# a.sort(key = lambda x : x.value())         dict doesnt have any sort() function....
# print(a)


a = {'apple':2,'banana':1,'cherry':3}
a.values()
print(a)
print(a['apple'])
d = {}
l = sorted(a.items(), key = lambda x : x[1])
print(l)
print(dict(l))
# for i in l:
#     d[i] = a[i]
# print(d)

