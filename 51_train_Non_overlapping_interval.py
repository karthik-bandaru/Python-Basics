a = [[1,3],[3,5],[5,7],[2,4]]

a.sort(key = lambda x : x[0])
# print(a)
for i in range(len(a)-1):
    if a[i][1] >= a[i+1][0]:
        print("False")
        break

# print("Hi")    
# print(a[1][1])

b = [[1,3],[3,5],[5,7],[2,4]]          
def is_platform_accomidate(a):                 
    a.sort( key = lambda x : x[0])      # to change in ascending order to arrival times 
    for i in range(len(a)-1):           # then [[1,3],[2,4],[3,5],[5,7]]
        if a[i][1] > a[i+1][0]:         # if the departute time is greater than nxt train of the arrival train
            return False                # here 1st train departure train is 3 and nxt arrival train is 2, then it returns False
    return True                         # bcz already train is there    
print(is_platform_accomidate(b))