 
def sqrtof(x):
    s = 0
    e = x + 1                     ## Here there is no need of e = x + 1 instead e = x
    while s < e :
        mid = (s + e) // 2
        
        if mid * mid > x :
            e = mid
        else:
            s = mid + 1
    print("The number is between {} and {}".format(s-1,s))        
    return s - 1
x = int(input("ENter ur number::"))
print(sqrtof(x))    


def sqrtt(x):
    s = 0
    e = x
    while(s<=e):
        mid = (s+e)//2
        if(mid*mid == x):
            return mid
        elif(mid*mid < x):
            s = mid + 1
        else:
            e = mid - 1
    print("{} is between the {} and {}".format(x,s,e))        
    return e   

print(sqrtt(8))