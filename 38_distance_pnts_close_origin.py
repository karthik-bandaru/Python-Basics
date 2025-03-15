def distance(arr):
    l = len(arr)
    J = len(arr[0])
    d = {}
    for i in range(l):
        k = 0
        for j in range(J):
            k = k + arr[i][j]**2
        dis = int(k**(0.5))
        d[i] = dis
    #print(d.items()) 
    return list(d.items())
 
def sort_distance(dist_list):
    n = len(dist_list)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if dist_list[j][1] < dist_list[min][1]:
                min = j
        dist_list[i],dist_list[min] = dist_list[min],dist_list[i]   # Here we change directly the tuplee
    # print(dist_list) 


    
a = [[3,3],[5,-1],[-2,4]]

dist_list = distance(a)
print(dist_list)

l = sorted(dist_list, key = lambda x : x[1])
print(l)

sort_distance(dist_list)

j = 0
k = 2
for i in range(len(dist_list)):
    if (j < k):
        m = dist_list[i][0]
        print(a[m])
        j+=1
    else:    
        break;  
