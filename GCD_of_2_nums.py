a=int(input("Enter the NUmberr::"))
b=int(input("Enter B number::"))
if(a>b):
    grt=a
    sml=b
else:
    grt=b
    sml=a

i=grt
while(grt>0):
    reminder = grt % sml
    if(reminder != 0):
        sml=reminder
        grt=sml
    else:
        print(sml)
        break;
