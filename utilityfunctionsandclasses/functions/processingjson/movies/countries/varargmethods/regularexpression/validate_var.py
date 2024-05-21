# validate python variable name
from re import*
var_name=input("enter a variable name")
pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")