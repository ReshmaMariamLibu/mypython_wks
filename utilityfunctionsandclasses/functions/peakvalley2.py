lst=[1,2,4,2,6,7,8,3]
count=0
p_count=0
v_count=0
for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]
    if x<y>z:
      p_count+=1
    elif x>y<z:
        v_count+=1
print(f"total no: of peaks={p_count},total no: valleys={v_count}")
