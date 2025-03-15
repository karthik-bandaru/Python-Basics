for i in range(65,91):
    print(chr(i),end = " ")

  

x = input("Enter the charecter")
if x.isalpha():
    print("the char %s is a alpha"%x)  

if((ord(x)>=65 and ord(x)<=90) or (ord(x)>97 and ord(x)<=122)):
    print("It is alphabet")
elif(int(x)>=0 and int(x)<=9):
    print("It is number")
else:
    print("It is special char ")
