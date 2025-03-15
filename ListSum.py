n = [[11,2,3],[4,15,6],[10,11,12],[7,8,19]]

def sum(l):
    s = 0
    for i in l:
        s += i
    return s    

def maxList(n):
    for i in range(len(n)-1):
        max = n[i]
        if( sum(n[i]) < sum(n[i+1]) ):
            max = n[i+1]

    return max

print(maxList(n))        

