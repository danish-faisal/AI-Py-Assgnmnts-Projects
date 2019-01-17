n=int(input("Enter a no. to check if its armstrong:"))
try:
   a=n
   m=0
   length=len(str(n))
   while n>0:
      i=n%10
      m+=i ** length
      n=n//10

   if m == a:
       print("armstrong no.")
   else:
       print("not an armstrong no.")

except ValueError:
   print("That's not a valid number,Try Again!")
