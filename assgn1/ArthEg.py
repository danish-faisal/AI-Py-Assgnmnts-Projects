
n=float(input("enter 1st number:"))
m=float(input("enter 2nd number:"))

if(m==0):
    print("2nd digit cant be 0\nPass new value")
    m=float(input("enter 2nd number:"))

print(n+m,"\n",n-m,"\n",n*m,"\n",n/m)
