#program to convert 12 hr clock into 24 hr clock



s="05:45:23PM"


r=s.split("PM")

temp=s[8:10]


if temp=="AM" and r[0][0:2]=="12":
    a=r[0][0:2]
    a="00"
    b=s[2:8]
    print(a+b)

if temp=="PM":
    
    a=r[0][0:2]
    b=s[2:8]
    a=int(a)
    if a>=1 and a<12:
        
        a=a+12
        a=str(a)
        print (a+b)
    else:
        a=str(a)
        print (a+b)
elif r[0][0:2]!="12":
    a=s[0:8]
    print (a)
