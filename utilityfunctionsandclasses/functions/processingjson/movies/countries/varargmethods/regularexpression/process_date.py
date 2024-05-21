from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\dates.txt")
pattern="\d{2}[-/]\d{2}[-/]\d{4}"
for line in f:
    date=line.rstrip("\n")
    matcher=fullmatch(pattern,date)
    if matcher!=None:
       print(date)
    
