# text="ABAACCBB"
#char count
# A:3,B:3,C:2

text=["hello", "hai","hello","hai","hello"]
#word count
#hello:3
# hai:2

wc={} #{"hello":3,"hai":2}
for w in text:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)



