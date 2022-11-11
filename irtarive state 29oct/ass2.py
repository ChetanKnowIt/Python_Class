a=int(input('Enter thr number'))
sum=0
while a!=0:
    b=a%10
    sum=b+sum
    a=a//10
else:
    print(sum)
