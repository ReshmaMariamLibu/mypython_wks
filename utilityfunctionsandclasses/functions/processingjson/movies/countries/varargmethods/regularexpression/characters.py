from re import*
#               101112
text="abcabABC K@&9eyz"
#     0123456789
#pattern="[a-d]" #matches either a,b,c,d
#pattern="[a-z]"  #matches either a,b,c,.....,z
# pattern="[A-Z]" matches uppercase A-Z
# pattern="[0-9]" matches digits
# pattern="[a-zA-Z0-9]" matches all alphanumeric characters
# pattern="[^a-z]" excludes all lowercase alphabets
# pattern="[^a-zA-Z]"# excludes all alphabets
# pattern="[^a-zA-Z0-9]" # matches all special characters

# predefined characters
# pattern="\d"  #[0-9]
# pattern="\D" excludes all digits[^0-9]
# pattern="\w" [a-zA-Z0-9] alphanumeric characters
pattern="\W"  #[^a-zA-Z0-9] excludes all alphanumeric characters


matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

