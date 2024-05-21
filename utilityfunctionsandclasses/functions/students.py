students=[
    {"rol":100,"name":"vijay","course":"django","marks":350,"gender":"m"},
    {"rol":101,"name":"ajay","course":"bigdata","marks":450,"gender":"m"},
    {"rol":102,"name":"bijoy","course":"django","marks":400,"gender":"m"},
    {"rol":103,"name":"hari","course":"bigdata","marks":250,"gender":"m"},
    {"rol":104,"name":"jhon","course":"testing","marks":220,"gender":"m"},
    {"rol":105,"name":"tinu","course":"django","marks":280,"gender":"m"},
    {"rol":106,"name":"vinu","course":"testing","marks":290,"gender":"m"},
    {"rol":107,"name":"abin","course":"django","marks":344,"gender":"m"},
    {"rol":108,"name":"riya","course":"bigdata","marks":360,"gender":"f"},
    {"rol":109,"name":"jini","course":"django","marks":480,"gender":"f"},
    {"rol":110,"name":"reshma","course":"testing","marks":200,"gender":"f"},

]

#print total number of student

print(len(students))

# print django students name

django_students=[st.get("name") for st in students if st.get("course")=="django"]
print(django_students)

#student name >300

mark_filter=[st.get("name")for st in students if st.get("marks")>=300]
print(mark_filter)

#django  female students name
gender_filter=[st.get("name")for st in students if st.get("course")=="django" and st.get("gender")=="f"]
print(gender_filter)

#top mark
top_student=max(students,key=lambda st:st.get("marks"))
print(top_student)

#min
lowest_mark=min(students,key=lambda st:st.get("marks"))
print(lowest_mark)
#sorted
srt=sorted(students,reverse=True,key=lambda st:st.get("marks"))
print(srt)

#print all courses
all_courses=[st.get("course") for st in students]
print(set(all_courses))


