text="Python is a high-level, general-purpose programming language"

# words=text.casefold().split(" ")
words=text.casefold().replace(",","").split(" ")


wc={}
for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)