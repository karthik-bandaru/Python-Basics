# a = [[1,3],[3,5],[5,7],[2,4]]
# r = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
# r = [1,1,2,3,4,5,6,10,11,12]
# if len(a) > len(b):
#     for i in range(len(b)):
#         if(a[i] >= b[i]):
#             r.append(b[i])
#         if(a[i] < b[i]):
#             r.append("Hii")
#             r.append(a[i])
#         r.append("N")    
# print(r) 


a = [1,3,5,6,10,12]
b = [1,2,4,11]
def combine_arrays_in_ascending_order(a,b):
    r = []
    i=j=0

    while(i<len(a) and j<len(b)):
        if(a[i]<=b[j]):
            r.append(a[i])
            i += 1

        else:
            r.append(b[j])
            j += 1
            
    while(i<len(a)):                     # Here if "i" value is still less than len(a) then remaining elements of a 
        r.append(a[i])                   # are append to r;
        i += 1

    while(j<len(b)):                     # If "j" is still less than len(b) then remaining elements of b
        r.append(b[j])                   # are append to r;
        j += 1
    
    return r

print(combine_arrays_in_ascending_order(a,b))


