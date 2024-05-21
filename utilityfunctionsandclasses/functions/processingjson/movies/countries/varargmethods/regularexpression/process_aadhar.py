from re import*
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\varargmethods\\regularexpression\\aadhdar.txt")
pattern="\d{4}\s?\d{4}\s?\d{4}"
for line in f:
    aadhar_no=line.rstrip("\n")
    matcher=fullmatch(pattern,aadhar_no)
    if matcher!=None:

     print(aadhar_no)