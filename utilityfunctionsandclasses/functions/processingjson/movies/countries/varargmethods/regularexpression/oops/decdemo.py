#decorator ->@property
# to access method as its property\attribute

class Employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept
    @property
    def get_name(self):
        return self.name
        
    @property
    def get_salary(self):
        return self.salary
        
emp=Employee("hari",50000,"HR")
print(emp.get_name)
print(emp.get_salary)
      