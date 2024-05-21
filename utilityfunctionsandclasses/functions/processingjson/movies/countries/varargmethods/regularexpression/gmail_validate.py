
from re import*
gmail_id=input("enter the gmail")
pattern="[a-z0-9_.]+@[a-z]{2,}.com"
matcher=fullmatch(pattern,gmail_id)
print("invalid"if matcher==None else "valid")