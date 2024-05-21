f1=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\allstudents.txt")
f2=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\failed.txt")

all_students={line.rstrip("\n") for line in f1}

failed_students={line.rstrip("\n") for line in f2}

passed_students=all_students.difference(failed_students)
print(passed_students)
print(all_students)
print(failed_students)