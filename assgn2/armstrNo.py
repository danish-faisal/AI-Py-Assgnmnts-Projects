n=int(input("Enter a no. to check if its armstrong:"))
a=n
m=0
while n>0:
   i=n%10
   m+=(i*i*i)
   n=n//10
if m==a:
    print("armstrong no.")
else:
    print("not an armstrong no.")
