# word="goodmorning"
# #g,o,n

# for ch in word:
#     cnt=word.count(ch)
#     if cnt>1:
#         print(ch)

word="hellooii"
srt_word=sorted(word)
count=len(word) 
for i in range(0,count-1):
      j=i+1
      if(srt_word[i]==srt_word[j]):
       print(srt_word[i])
   
      

