from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\lang.txt")
pattern="[k-n][369]{1}[a-zA-Z0-9]*"
for line in f:
    lang=line.rstrip("\n")
    matcher=fullmatch(pattern,lang)
    if matcher!=None:
        print(lang)