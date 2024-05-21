from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\date1.txt")
# pattern="(20)([01][0-9]|2[0-3])[-/]\d{2}[-/]\d{2}"
pattern="(20)([01][0-9]|2[0-3])[-/](0[1-9]|1[0-2])[-/]([0][1-9]|[12][0-9]|3[01])"
for line in f:
    date=line.rstrip("\n")
    matcher=fullmatch(pattern,date)
    if matcher!=None:
         print(date) 