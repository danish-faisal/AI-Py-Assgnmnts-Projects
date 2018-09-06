#Complex Number Class
class CompNo:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,cmpno):
        self.real=self.real+cmpno.real
        self.imag=self.imag+cmpno.imag
    def sub(self,cmpno):
        self.real=self.real-cmpno.real
        self.imag=self.imag-cmpno.imag
    def __str__(self):
        return (str(self.real)+"+i"+str(self.imag))

#Employee Class
class Employee:
    def __init__(self,name,salary,isSen):
        self.name=name
        self.salary=salary
        self.isSen=isSen
    def isAsen(self):
        if(self.isSen):
            print("I am a senior employee")
        else:
            print("I am a junior employee")

c1=CompNo(2,4)
c2=CompNo(4,8)
c1.add(c2)
print(c1)
c2.sub(c1)
print(c2)
e1=Employee("A",2000,True)
e2=Employee("B",3000,False)
e1.isAsen()
e2.isAsen()
