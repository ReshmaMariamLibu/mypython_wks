f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\data.txt","r")
h=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\years.txt","w")
for line in f:
    y=int(line.rstrip("\n"))
    if y%100==0 and y%400==0:
        h.write(str(y)+"\n")
    elif y%100!=0 and y%4==0:
        h.write(str(y)+"\n")
f.close()
h.close()
