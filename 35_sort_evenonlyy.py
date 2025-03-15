'''a = [6,12,5,10,19,23,4,8]
#output = [4,6,5,8,19,23,10,12]
def sorting(a):
    L = len(a)
    x = [0]*L
    # for i in range(L):
    #     min = i
    #     for j in range(i+1,L):
    #         if a[i] % 2 != 0:
    #             x.insert(i,a[i])
    #             break
    #         if a[j] < a[min]:
    #             min = j
    #     x[i],a[min] = a[min],a[i]
    a.sort()

    for i in range(L):
        if a[i] % 2 != 0:
            
    return x 
print(sorting(a))'''

# a = [6,12,5,10,19,23,4,8]
# even = []
# L = len(a)
# arr = [0]*L
# for i in range(L):
#     if a[i] % 2 == 0:
#         even.append(a[i])
#     else:
#         arr[i] = a[i]
# even.sort()        
# print(arr)
# print(even)     
# E_Len = len(even)
# print(E_Len)
# n = 0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         arr[i] = even[n]
#         n += 1    
# # k=0
# # n=0
# # while(k<5):
# #     if arr[k] == 0:
# #         arr[k] = even[n]
# #         k += 1
        


# print(arr)      



def sort_even_only(a):
    L = len(a)         
    even_list = []
    sort_list = [0]*L                                   # sort_list = [0,0,0,0,0,0,0,0]
    for i in range(L):
        if a[i] % 2 == 0:
            even_list.append(a[i])
        else:
            sort_list[i] = a[i]                         # sort_list = [0,0,5,0,19,23,0,0]
                                   
    even_list.sort()                                    # odd nums settled in their respective places..
    
    n = 0                                               # for number of even elems
    for i in range(L):
        if sort_list[i] == 0:
            sort_list[i] = even_list[n]
            n += 1
    return sort_list

a = [22,23,25,3,6,15,2,4,9,17,1,8,12]
print(sort_even_only(a))  





'''
sort even nums but odd nums should be in their place only
'''
arr = [6,12,5,10,19,23,4,8] 
       #4 6 5 8 19 23 10 12     
       
def result(arr):
    even_nums = sorted([i for i in arr if i%2 == 0])
    res = []
    even_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            res.append(even_nums[even_index])
            even_index += 1
        else:
            res.append(arr[i])
    return res 
    
print(result(arr))
                                        
      




