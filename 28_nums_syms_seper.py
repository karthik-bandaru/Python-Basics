a=["1","/","-212","+","-67","-"]
def list_strings(L):
    num=[];sym=[]
    for i in a:
        try:
            if int(i)<=0 or int(i)>0:
                num.append(int(i))
        except ValueError:
            sym.append(i)
    num.sort()
    return num,sym;

print(list_strings(a))
# print(type(a[2]))
# print(int("-212"))

numbers=[]
sign=[]
a = ["1","/","-212","+","-67","-"]
def is_digit(num):
    if num.isdigit():
        numbers.append(int(num))

    elif ( num.startswith("-") and len(num) > 1 ):  # in "-67" len is 3 and to avoid like "-" len is 1 
        t = int(num[1:])
        numbers.append(-t)
    
    else:
        sign.append(num)

for i in a:
    is_digit(i)

numbers.sort()
print(numbers)
print(sign)


# t=int(n[1:])
# print(-t)