# for i in range(1,25):

#     if i==10:
#         break
#     print(i)

# print("program execution is completed")

lst=[10,11,12,14,15]
num=3
for i in range(0,len(lst)):
    if num==lst[i]:
      print("element found")
      break
else:
   print("element not found")