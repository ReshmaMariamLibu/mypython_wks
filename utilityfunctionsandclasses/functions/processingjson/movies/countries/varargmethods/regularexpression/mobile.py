#rule for validating mobile numbers
from re import*
mob_num=input("enter the mob number")
pattern="(91)?[0-9]{10}"
matcher=fullmatch(pattern,mob_num)
print("invalid"if matcher==None else "valid")