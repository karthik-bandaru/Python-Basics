#input = ["apple","banana","pear","kiwi"]
#output = ["pear","kiwi","apple","banana"]
a = ["apple","banana","pear","kiwi"]
n = len(a) 

for i in range(n):                             # a.sort(key = len)
    min = i                                    # print(a) 
    for j in range(i+1,n):                     # Then we get the output directly....
        if len(a[j])< len(a[min]):
            min = j
    a[i],a[min] = a[min],a[i] 
print(a)

a.sort(key = lambda x : len(x))
print(a)








