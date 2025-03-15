decimal_num=int(input("Enter the Decimal NUmeber::"))
binary_num=0
i=0
while(decimal_num!=0):
    reminder=decimal_num%2
    binary_num=binary_num+reminder*(10**i)
    decimal_num=decimal_num/2
    i=i+1
print(binary_num)    