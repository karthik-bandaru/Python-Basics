a = {}
s = "karthikkeya"

for i in (s):
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1    

print(a)        