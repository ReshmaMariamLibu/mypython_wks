from re import*
text=input("enter the  pan number")
pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(pattern,text)
print("invalid"if matcher==None else "valid")

#qs
#q1 rule for validation aadhar no =>valid 3218 0565 8789  valid 321805658789
#q2 kerala vechicle registration no => valid KL-08-A 1,2-DIGIT 4