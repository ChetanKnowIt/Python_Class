a,b,c,d,e=input("enter marks").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
avg=(a+b+c+d+e)/5
print(avg)
if avg>40:
    if avg>70:
        print('distinction')
    elif  avg>60 and avg<70:
        print('First division')
    else:  
        print('Second division')
else:
    print('Fail')
   
