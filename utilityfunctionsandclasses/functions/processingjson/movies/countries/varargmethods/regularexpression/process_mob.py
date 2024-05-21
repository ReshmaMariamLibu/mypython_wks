from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\mob.no.txt")
pattern="(91)?[0-9]{10}"
for line in f:
    pan_no=line.rstrip("\n")
    matcher=fullmatch(pattern,pan_no)
    if matcher!=None:
        print(pan_no)