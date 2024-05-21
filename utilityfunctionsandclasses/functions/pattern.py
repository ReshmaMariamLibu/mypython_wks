text="ABABC"

lst=[]


for ch in text:
    
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:
        non_recursive.append(ch)

print(non_recursive[1])



    
    
