from re import*
text="abaabcaabaaaa"

# pattern="a+" # + atleast one a
# pattern="a*"  # matches for any no: of a
# pattern="a?"  #optional
# pattern="a{2}"  #specifies occurence of a as 2 times
pattern="a{2,3}" #matches min 2 'a' ,max 3 'a'
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())


