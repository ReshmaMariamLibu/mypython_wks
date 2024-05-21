#re.py-regular expression
#def finditer()-to find location of specified pattern
from re import*
text="ababcdABabac"
pattern="ab"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start())
    print(m.group())
    count+=1
print("occurence of pattern=",count)

    
