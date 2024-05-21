lst=[10,2,14,5,6,8,9]
element=int(input("enter the number"))
lst.sort()
low=0
upp=len(lst)-1
is_present=False
while(low<=upp):
    mid=(low+upp)//2

    if(element==lst[mid]):
        is_present=True
        break
    elif element>lst[mid]:
        low=mid+1
    elif element<lst[mid]:
        upp=mid-1
print(is_present)