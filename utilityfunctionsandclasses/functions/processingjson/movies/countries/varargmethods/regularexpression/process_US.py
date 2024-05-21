from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\US.txt")
pattern="[0-9]{3}[-]?[0-9]{3}[-]?[0-9]{4}"
for line in f:
    US_no=line.rstrip("\n")
    matcher=fullmatch(pattern,US_no)
    if matcher!=None:
        print(US_no)