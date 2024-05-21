f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\data.txt","r")
#open("filepath","file reference")

words=[line.rstrip("\n") for line in f]
print(words)

