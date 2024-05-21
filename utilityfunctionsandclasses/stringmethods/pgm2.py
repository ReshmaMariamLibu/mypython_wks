words="pneumonoultramicroscopicsilicovolcanoconiosis"
length=len(words)
count=0
for ch in words:
    print(ch)
    if ch=='a':
        count+=1
    elif ch=='e':
        count+=1
    elif ch=='i':
        count+=1
    elif ch=='o':
        count+=1
    elif ch=='u':
        count+=1
print(f"number of vowels is {count}")
conso=length-count
print(f"number of consonents is {conso}") 

#vowels='a','e','i','o'.'u'
#v_count=0
#c_count=0

# for ch in words:
#     if ch in vowels:
#         v_count+=1
#     elif ch.isalpha():
#        c_count+=1
# print(f"total no: of characters {len(words)}")
#print(f"total no: of vowels {v_count} ")
#print(f"total no: of consonents {c_count}")
   
     