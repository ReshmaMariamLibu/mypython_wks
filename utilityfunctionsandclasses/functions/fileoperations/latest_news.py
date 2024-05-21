f_news=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\latest_news.txt","r")
f_stop=open("C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\fileoperations\\stopwords.txt","r")

news_words=set()
stop_words={line.rstrip("\n") for line in f_stop}
print(stop_words)

for line in f_news:
    words=line.split()
    for w in words:
        news_words.add(w)
print(news_words.difference(stop_words))

