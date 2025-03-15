a="He ll o wo rl d"
b="i am ka rthik"


a_count = a.count(" ")
b_count = b.count(" ")

diff = abs(a_count - b_count)

if diff % 2 == 0:
    print(f"Even{diff}")
else:
    print(f"Odd{diff}")

'''
acount=0
for i in a:
    if i==" ":
        acount+=1
bcount=0        
for j in b:
    if j==" ":
        bcount+=1

if(acount>=bcount):
    res=acount-bcount
else:
    res=bcount-acount    

if(res%2==0):
    print("Even {}".format(res))
else:
    print("Odd {}".format(res))    
    '''