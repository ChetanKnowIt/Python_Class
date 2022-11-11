a,b,c=input('enter no').split()
a=int(a)
b=int(b)
c=int(c)
if a>b:
    if a>c:
        print('a is gtr')
    else:
        print('cis gtr')
elif b>c:
    print('b is grt')
else:
    print('c is grt')
