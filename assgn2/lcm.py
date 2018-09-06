a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
for i in range(1,a*b+1):
    if ((i%a==0) and (i%b==0)):
        print("LCM is ",i)
        break
