#starting with an alphabet k,l,m,n
#second that must be a digit and divisible by 3
#followed by any no: of alphabets and digits
from re import*
varname=input("enter a variable name")
pattern="[k-n][369][a-zA-Z0-9]*"
matcher=fullmatch(pattern,varname)
print("invalid"if matcher==None else "valid")