#functions1.py--assignment
var=10
def check(n):
    global var
    if n==var:
        print("yes")
    else:
        print("no")


#functions2.py--assignment
def prtstr(txt,n):
    for i in range(0,n):
        print(txt)
    print("end")

#functions3.py--assignment
def recr(n):
    if n>0:
        print(n)
        recr(n-1)

check(4)
check(10)
prtstr("MSND",4)
recr(4)
