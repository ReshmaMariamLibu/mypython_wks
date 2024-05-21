from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\vech.txt")
pattern="(KL)[-\s]?[\d]{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"
for line in f:
    veh_no=line.rstrip("\n")
    matcher=fullmatch(pattern,veh_no)
    if matcher!=None:

     print(veh_no)