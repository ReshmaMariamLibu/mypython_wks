from re import*
text=input("enter the mob number")
pattern="[0-9]{3}[-]?[0-9]{3}[-]?[0-9]{4}"
matcher=fullmatch(pattern,text)
print("invalid"if matcher==None else "valid")