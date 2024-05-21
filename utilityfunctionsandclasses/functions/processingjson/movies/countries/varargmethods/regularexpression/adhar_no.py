from re import*
aadhar_no=input("enter the number")
pattern="\d{4}\s?\d{4}\s?\d{4}"
matcher=fullmatch(pattern,aadhar_no)
print("invalid"if matcher==None else "valid")