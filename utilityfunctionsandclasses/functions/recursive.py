text="ABABC"

lst=[]
duplicate_lst=[]

for ch in text:
    
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:
        duplicate_lst.append(ch)

print(duplicate_lst[1])


text="ABACCD"

lst=[]
for ch in text:
    
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:  
     print(f"first two  {ch}")
     break
    
    
