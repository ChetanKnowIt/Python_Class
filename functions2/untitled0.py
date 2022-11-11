def sayHi():
    print("Hi")
    
sayHi()


def sayHi(name):
    """ This function will say Hi"""
    print("Hi ",name)
    
sayHi("Trupti")

print((sayHi.__doc__))

print(help(sayHi))


print(type(sayHi))

temp=sayHi
print(temp("Ishwari"))



def calculation(a,b):
    print(a+b)
    
calculation(2,3)
calculation(2.5,3.4)
calculation(2,3.4)
calculation(12.1,3)
calculation("Hi"," Tina")
calculation((2,3),(10,20))
calculation([2,3,4],[10,20])


def cal(a,b):
    return a+b, a-b,a*b

add, sub,mul=cal(10,5)
print(add, sub,mul)

temp=cal(10,5)
print(temp)

add, *res=cal(10,5)
print(add, res)

a,*res=cal(10,5)
print(res)


#---------------------------------
#Required
def display(lst):
    print(lst[::2])
    
display([1,2,3,4,5,6])
display()
    
    



#Default Function

def display(no=20,lst=[10,20,3,2,40]):
    for i in lst:
        if i>no:
            print(i)
    
display(3,[1,2,3,4,5,6])
print('-'*20)
display(10)
print('-'*20)
display()

#Keyword

display(lst=[1,2,3,4,5],no=3)

display(lst=[1,2,300,400,500])


#Variable length
#*arg
def disString(a,*array):
    print(a)
    for i in array:
        print(i)
        
disString("IN Function",10,20, 30,40,50)


def disString(a,*array):
    print(a)
    print(type(array))
    if a==1:
        print(sum(array))
    elif a==2:
        print(len(array))
    elif a==3:
        fact=1
        for i in array:
            fact=fact*i
        print(fact)
        
disString(1,10,20, 30,40,50)
disString(2,10,20, 30,40,50,10,20, 30,40,50)
disString(3,10,20)

#-------------------------
# **args
def DisplayModule(**args):
    print(args)
    for i in args.items():
        print(i)

DisplayModule(maths=23,java=34,c=34)
print("-"*20)
DisplayModule(hindi=23,marathi=34,Telgu=34)


#----------------------------------
fun=lambda a:a*a
print(fun(3))


fun=lambda a,b:a+b
print(fun(3,3))
print(fun(3.6,3.8))
print(fun(4.3,3))
print(fun("we ","happy"))


fun=lambda a,*b:a+sum(b)
print(fun(3,3,4,5,6))
print(fun(3.6,3.8,3,6.7,8))

fun=lambda a,*b:a+b
print(fun((3,),3,4,5,6))


print(abs(-3))

l=200
s=400

lst=[l>1000,s>500]
print(lst)
if all(lst):
    print("Good going!!!")
elif any(lst):
    print("ok ok")
else:
    print("keep it up!!!")


print(eval('34+5'))

k=eval('34+5')
print (k,type(k))


eval('print(12345)')


#------------------------------
#map
lst=["hi","hello","welcome","hi","hello","welcome","hi","hello","welcome","hi","hello","welcome","hi","hello","welcome"]
lst1=list(map(len,lst))
print(lst1)
#-------------------------------



def slice(s):
    return s[::2]

lst=["hi1","hello1","welcome1"]
lst3=list(map(slice,lst))
print(lst3)

#-------------------------------
lst=["hi1","hello1","welcome1"]
lst3=list(map(lambda s:s[::2],lst))
print(lst3)

#-------------------------------

lst=["hi1","hello1","welcome1"]
lst3=list(map(lambda s:s[::-1],lst))
print(lst3)



lst=["hi1","hello1","welcome1"]
lst3=list(map(lambda s:s[::-1][::2],lst))
print(lst3)

#-------------------------------

a,b,c = map(int,input("Enter for 3 sub: ").split())
print(a,b,c)

print("=="*20)

d=list(map(int,input("Enter for 3 sub: ").split()))
print(d)

#==========================================
def Positive(a):
    return a>0
l1=[1,-3,5,6,-4,6,-2]
l2=list(filter(Positive,l1))
print(l2)

print('='*50)

l1=[1,-3,5,6,-4,6,-2]
l2=list(filter(lambda a:a>0,l1))
print(l2)



lst=["hi1","hello","welcome1","we","welcome1welcome1"]
l2=list(filter(lambda a:len(a)>3,lst))
print(l2)
lst=["hi1","hello1","welcome1","@@@","welcome1welcome1"]
l2=list(filter(str.isalnum,lst))
print(l2)
print(len(l2))





