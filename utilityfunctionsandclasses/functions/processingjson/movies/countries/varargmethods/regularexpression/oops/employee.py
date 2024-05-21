#set_employee->snakecase
class Employee:
    id:int
    name:str
    dept:str
    salary:int


    def __init__(self,id,name,dept,salary):
        #instance variable is the attribute
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary

    def display(self):
        print(self.id,self.name,self.dept,self.salary)

    def __str__(self):
        return self.name


#creation of object
#reference_name=ClassName()
emp1=Employee(1000,"vinay","manager",1200000)
print(emp1)
# emp1.set_employee(1000,"vinay","manager",1200000)
# emp1.display()

# emp2=Employee()
# emp2.set_employee(2000,"geena","HR",1100000)
# emp2.display()