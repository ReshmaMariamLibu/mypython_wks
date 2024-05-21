from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\pan.txt")
pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"
for line in f:
  pan_no=line.rstrip("\n")
  matcher=fullmatch(pattern,pan_no)
  if matcher!=None:
    print(pan_no)