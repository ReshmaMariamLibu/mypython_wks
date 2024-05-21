frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

for fw in frameworks:
      print(fw.get("name"))

for fw in frameworks:
      print(fw.get("rating"))

#using list comprehension

# fw_names=[fw.get("name")for fw in frameworks ]
# print(fw_names)

all_ratings=[fw.get("rating")for fw in frameworks ]
print(all_ratings)

# #print python frameworks name

py_fwnames=[ fw.get("name") for fw in frameworks if fw.get("language")=="python" ]
print(py_fwnames)

# #rating =5 fw names
# rating_filter=[fw.get("name")for fw in frameworks if fw.get("rating")==5] 
# print(rating_filter)

# #id 1 to 3
# id_filter=[fw.get("name")for fw in frameworks if fw.get("id") in range(1,4) ]
# print(id_filter)

#min,max,sort

lowest_rating=min(frameworks,key=lambda fw:fw.get("rating"))
print(lowest_rating)

top_rating=max(frameworks,key=lambda fw:fw.get("rating"))
print(top_rating)

srt=sorted(frameworks,reverse=True,key=lambda fw:fw.get("rating"))
print(srt)