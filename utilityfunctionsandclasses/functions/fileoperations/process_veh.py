f_read=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\vehicle_numbers.txt")
f_write=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\kerala_numbers.txt","w")

for line in f_read:
    reg_num=line.rstrip("\n")
    if reg_num.startswith("kl"):
        f_write.write(reg_num+"\n")