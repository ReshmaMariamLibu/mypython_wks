from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\var.txt")
pattern="[a-zA-Z][a-zA-Z0-9_]*"
for line in f:
    var=line.rstrip("\n")
    matcher=fullmatch(pattern,var)
    if matcher!=None:
        print(var)