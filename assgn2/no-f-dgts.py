n=int(input("Enter a number:"))
m=n
count=1
while n>9:
    count=count+1
    n=n//10
print(m," is a ",count," digit no.")
