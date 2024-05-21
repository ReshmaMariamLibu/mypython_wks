#write a regular expression for validating yyyy-mm-dd
from re import*
date_no=input("enter the number")
pattern="\d{4}[-]\d{2}[-]\d{2}"
matcher=fullmatch(pattern,date_no)
print("invalid"if matcher==None else "valid")