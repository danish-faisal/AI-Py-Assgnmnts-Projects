def print_menu():
    print("Enter:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division")

choice=True
while(choice):
    print("Enter 1st Number:")
    m=float(input())
    print("Enter 2nd Number:")
    n=float(input())
    print_menu()
    x=int(input())
    if(x==1):
        print("Result:",m+n)
    elif(x==2):
        print("Result:",m-n)
    elif(x==3):
        print("Result:",m*n)
    elif(x==4):
        try:
            print("Result:",m/n)
        except:
            print("Division by 0 error.Try Again")
    else:
        print("Invalid Choice.Try Again")
        continue

    print("Do you want to continue?(y/n):")
    c=input()
    if(c=='n'):
        choice=False
        
