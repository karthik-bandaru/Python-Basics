# a = 'k'                                                   # chr(67)  = C
# print(ord('A'),ord('Z'))                                  # ord(C) = 67      

# s = "hellogoodmorningkk"

# n = 5
# a = [s[i:i+5] for i in range(0,len(s),5)]

# for i in range(len(a)):

#     if i%2 != 0:                                                  # to find odd or even position 
#         a[i] = "".join(sorted(a[i], key = lambda x : x[0:],reverse=True))
#     else:
#         a[i] = "".join(sorted(a[i], key = lambda x : x[0:],reverse=False))
# print("".join(a))
# a = ["mhii","karthi"]
# a[1] ="".join(sorted(a[1], key = lambda x : x[0:]))
# print(a)







s = "helloguysiamfromdharmavaram"
n = int(input("Enter Number to divide that stringss :: "))

def divide_string_and_sorting(string,n):


    #  HelloGuysIamfromDharmavaram
    # we have to divide string as n charecters soo...           if n = 5

    L = [string[i:i+n] for i in range(0,len(string),n)]         # L = ["Hello","GuysI","amfro","mDhar","mavar","am"]

    print("After dividing the string into {} charectes =  {}".format(n,L))


                                                                # Now we have to sort the chars in descending order at odd position list L 
    for i in range(len(L)):
        if i%2 != 0:                                             #To find the odd position
            L[i] = "".join(sorted(L[i], key = lambda x : x[0:], reverse = True))
        else :
            L[i] = "".join(sorted(L[i], key = lambda x : x[0:], reverse = False))     #This is for to sort the chars in even position

    print("List is ",L)                                      #['ehllo','yusig','afmor','rmhda','aamrv','ma']
    return "".join(L)                                        # ehlloyusigafmorrmhdaaamrvma

print(divide_string_and_sorting(s,n))


# s = "helloguysiamfromdharmavaram"
# n = int(input("Enter the Number to divide the string : "))

def divide_str_and_sort_str(str,n):
    
    l = [str[i:i+n] for i in range(0,len(str),n)]

    for i in range(len(l)):
        if i%2 != 0:
            l[i] = "".join(sorted(l[i], key = lambda x : x[0:], reverse=True))
        else:
            l[i] = "".join(sorted(l[i], key = lambda x : x[0:], reverse=False))

    print("List is ",l)
    return "".join(l)
print(divide_str_and_sort_str(s,n))    


