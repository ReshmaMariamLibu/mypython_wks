# text="ABAACCBB"
# wc={}
# for ch in text:
#     if ch not in wc:
#         wc[ch]=1
#     else:
#         wc[ch]+=1
# print(wc)

text="ABAACCBBDEF"
wc={}
for ch in text:
     if ch not in wc:
        wc[ch]=1
     else:
        wc[ch]+=1
print(wc)

# print non-repeating chracters
for k,v in wc.items():
    if v==1:
      print(k)
