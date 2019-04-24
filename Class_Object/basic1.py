
class Employee:

    '''
    This is the student class
    '''

    def details(self,eno,ename,esal):
        self.empno=eno
        self.empname=ename
        self.empsal=esal

    def info(self):
        print("Employeename", self.empname)
        print("Employeenumber",self.empno)
        print("Employeesalary",self.empsal)
    def getself(self):
        print("value of self is "+str(self))


e=Employee()
e.details("a123","Prashant","12345678")
e.info()

print(Employee.__doc__)
'''help(class_name ) this will give all the information about the class'''
help(Employee)

''''
self refers to the same address as e refers 

'''
print("value of e is "+str(e))
e.getself()