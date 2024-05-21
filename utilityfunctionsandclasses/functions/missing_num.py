lst=[1,2,4,5,6]
# max_num=max(lst)

# total_sum=max_num*(max_num+1)/2
# curr_sum=sum(lst)

# diff=total_sum-curr_sum

# if(diff==0):
#     print(max+1,"is least +ve missing number")
# else:
#     print(diff,"is missing number")

lmt=len(lst)-1
i=0
while(i<lmt):
  j=i+1
  diff=lst[j]-lst[i]
  if(diff==1):
    i+=1
  else:
    print(lst[i]+1,"is missing")
    break