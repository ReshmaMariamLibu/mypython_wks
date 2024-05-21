from re import*
vech_no=input("enter the number")
pattern="(KL)[-\s]?[\d]{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"
matcher=fullmatch(pattern,vech_no)
print("invalid"if matcher==None else "valid")