#sum-of-digits of the given no.
def sumofdig(n,store):
    if n>0:
        sumofdig(n//10,store+n%10)
    else:
        print(store)

#factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

sumofdig(54321,0)
x=fact(4)
y=fact(6)
print(x,"\n",y)
