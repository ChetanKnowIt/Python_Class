a=int(input())
rev=0
while a!=0:
    mod=a%10
    rev=rev*10+mod
    a=a//10
else:
    print(rev)
