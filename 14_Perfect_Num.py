# Perfect means 6 = 1 + 2 + 3 
# It means "" The sum of the factors of the given Numberrr "" Except Itself::

n=int(input("Enter the NUmberr::"))
m=n

def factors(n):
    sum=0
    for i in range(1,n):                        # if we enter the range as "n+1" then itself factor printedd
        if(n%i==0):                             # Otherwise the last factor i.e., ""n"" is printed.....
            sum=sum+i
    if(sum==n):
        print("{} is a Perfect Number".format(n))
    else:
        print("{} is not a Perfect Numberr...".format(n))
        
                    
factors(n)

