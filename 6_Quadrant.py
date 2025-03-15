x=int(input("Enter the value of X coordinate::"))
y=int(input("Enter the value of Y coordinate::"))
if(x>0 and y>0):
    print("(%d,%d) is lies in 1st qudrant".format(x,y))
elif(x<0 and y>0):
    print("(%d,%d) is lies in 2nd qudrant".format(x,y))
elif(x<0 and y<0):
    print("(%d,%d) is lies in 3rd qudrant".format(x,y))
elif(x>0 and y<0):
    print("(%d,%d) is lies in 4th qudrant".format(x,y))
elif(x==0 and y==0):
    print("(%d,%d) lies on origin".format(x,y))
elif(x==0 and y>0):
    print("(%d,%d) is lies on +ve Y-axis".format(x,y))
elif(x==0 and y<0):
    print("(%d,%d) is lies on -ve Y-axis".format(x,y))
elif(x>0 and y==0):
    print("(%d,%d) is lies on +ve X-axis".format(x,y))    
elif(x<0 and y==0):
    print("(%d,%d) is lies on -ve X-axis".format(x,y))