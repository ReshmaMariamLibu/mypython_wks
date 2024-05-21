expenses=[12000,11000,24000,25000,45000,23000,21000]
# count=len(expenses)
# for i in range(0,count):
#     print(expenses[i])

# expenses[1]=15000
# print(expenses)
total=0
for i in range (0,len(expenses)):
    total=total+expenses[i]
print(total)

#total
total=sum(expenses)
print(total)

#min
srt_exp=min(expenses)
print(srt_exp)

#sorting
#expect 0->true
#0->false
srt_exp=sorted(expenses,reverse=True)
print(srt_exp)