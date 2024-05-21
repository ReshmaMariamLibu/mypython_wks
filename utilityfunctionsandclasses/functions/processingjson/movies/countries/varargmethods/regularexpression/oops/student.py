# student rolnum,course,total

class Student:
    rolnum:int
    course:str
    total:str


    def __init__(self,rolnum,course,total):
        self.rol=rolnum
        self.course=course
        self.total=total

    def display(self):
        print(self.rol,self.course,self.total)

obj1=Student(100,"django",500)
obj1.display()