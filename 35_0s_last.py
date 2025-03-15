# a = [0,1,2,0,3,4,0,6,7]
# b = []
# c = []
# for i in a:
#     if i != 0:
#         b.append(i)
#     else:
#         c.append(i)
# b.extend(c)
# print(b)

# a = [0,1,2,0,3,4,0,6,7]
# b = [i for i in a if i == 0]          It is also one type
# c = [i for i in a if i != 0]    
# print(c+b)

# c = 0
# for i in range(len(a)):
#     if a[i] == 0:
#         c += 1
# print(c)
# print(a+[0]*c)        



# def send_zero_last(a):
#     L = len(a)
#     num = [i for i in range()]

a  = [0,1]

def sort_only_num(a):
    L = len(a)
    for i in range(L):
        if a[i] == 0:
            for j in range(i,L-1):
                a[j] = a[j+1]
            a[L-1] = 0 
    return a 
           


print(sort_only_num(a))


def send_zero_to_last(a):

    c = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[c] = a[i]        #### to send elems forwarddddd
            c += 1             #### to count how many elems are shifted  that means non zero elems count.
    for i in range(c,len(a)):
        a[i] = 0

    return a

print(send_zero_to_last(a))

    

    
    