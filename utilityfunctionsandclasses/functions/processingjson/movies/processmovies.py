from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\db.json"
with open(path)as f:
    data=load(f)
#print(len(data))
all_names=[m.get("Title")for m in data]
#print(all_names)

# print all directors name

all_directors={m.get("Director") for m in data}
all_directors.discard("N/A")
#print(all_directors)

# highest IMDB rating

filtered_data=[ m for m in data if m.get("imdbRating") !="N/A"]
top_movie=max(filtered_data,key=lambda m:float(m.get("imdbRating")))
#print(top_movie.get("Title"))

#print all generes
#print all movie with genere action
#movies released before 2014

# all_genre={ m.get("Genre")for m in data}
# print(all_genre)

all_geners=set()
for m in data:
    for gn in m.get("Genre").split():
        all_geners.add(gn.rstrip(","))
print(all_geners)

# for mv in data:
#     if mv.get("Genre").count("Action")>0:
#         print(mv.get("Title"))

#movies released after 2014
for mv in data:
    r_date=mv.get("Released")
    year=r_date.split(" ")[-1]
    if year.isdigit():
        if int(year)>2014:
            print(mv.get("Title"),mv.get("Released"))



