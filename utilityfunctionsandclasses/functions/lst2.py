# lst=[2,4,5,6]
# sum=7
# for i in range(0,len(lst)):
#  for j in range(i+1,len(lst)):
#     if lst[i]+lst[j]==sum:
#        print("pairs",lst[i],lst[j])


sum=int(input("enter sum>"))
arr=[2,4,5,6,8]
arr.sort()
low=0
upp=len(arr)-1
while(low<upp):
   curr_sum=arr[low]+arr[upp]

   if curr_sum==sum:
      print("pairs",arr[low],arr[upp])
      low+=1
      upp-=1
   elif curr_sum<sum:
    low+=1
   elif curr_sum>sum:
    upp-=1




