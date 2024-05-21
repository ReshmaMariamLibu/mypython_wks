prev=0
cur=1
print(prev)
print(cur)
i=1
while(i<=10):
    next=prev+cur
    print(next)
    prev=cur
    cur=next
    i+=1
    