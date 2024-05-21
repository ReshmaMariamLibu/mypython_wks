f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\news.txt")
wc={}
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1
print(wc)