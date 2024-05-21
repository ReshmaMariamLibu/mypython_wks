from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\countries\\data.json"

with open(path,encoding="utf-8") as f:
    data=load(f)
print(len(data))

all_region={c.get("region")for c in data}
# print(all_region)

asian_countries=[c.get("name")for c in data if c.get("region")=="Asia"]
# print(asian_countries)

#print independent country names
# independent_countries=[c.get("name")for c in data if c.get("independent")==True]
# print(independent_countries)

#print (independent_countries)
# independent_countries=(c.get("independent")for c in data if c.get("region")==)
# print(independent_countries)

#name of country with highest population

pop_country=max(data,key=lambda c:c.get("population"))
# print(pop_country.get("name"))

# name of countries sharing borders with india

india_borders= [c.get("name")for c in data if c.get("borders")=="IND" ]
print(india_borders)