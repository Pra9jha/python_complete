
'''self mean current object ,so if we are calling method with e
 then self = e else if we are calling from e1 then e1 = self
 '''



class Employee:

    def __init__(self,eno,ename,esal):
        print(id(self))
        self.empno=eno
        self.empname=ename
        self.empsal=esal

    def info(self):
        print("Employeename", self.empname)
        print("Employeenumber", self.empno)
        print("Employeesalary", self.empsal)

e=Employee("a123","Prashant","12345678")
print(id(e))
print("*"*20)
e1=Employee("b123we","Prabhat","2345678899")
print(id(e1))
e.info()
print("*"*20)
e1.info()



