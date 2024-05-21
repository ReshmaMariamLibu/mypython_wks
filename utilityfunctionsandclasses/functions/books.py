

class Books:
       
           data=[
                   {"id":100,"name":"python","price":350},
                   {"id":101,"name":"java","price":450},
                   {"id":102,"name":"django","price":1300},
                   {"id":103,"name":"html","price":1000},
                   {"id":104,"name":"bootstrap","price":300},




           ]

for fw in Books:
      print(fw.get("name"))

          

all_books=[fw.get("books")for fw in Books ]
print(all_books)
py_language=[fw.get("language") for fw in frameworks  fw.get("language")=="python"]
print(py_language)

all_books=[st.get("name") for st in Books if st.get("course")=="django"]
print(all_books)















