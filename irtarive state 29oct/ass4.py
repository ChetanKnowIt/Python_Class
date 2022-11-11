#palindrome
a=int(input('Enter number'))
print(a)
rev=0
a=int(a)
while a!=0:
    mod=a%10
    rev=rev*10+mod
    a=a//10

    if rev==a:
        print("palindrome")
        break
        
else:
        print('not palindrome')
    
