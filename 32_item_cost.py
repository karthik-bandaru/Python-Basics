a = input("Enter the Value::")
cost=1
for i in a:
    if int(i)==0:
        continue
    cost = cost*int(i)
print("Cost of a Product is ",cost)    

b = int(input("Enter Number : "))
c = 1
while(b>0):
    r = b%10
    if(r != 0):
        c *= r
    b = b//10

print(c)        