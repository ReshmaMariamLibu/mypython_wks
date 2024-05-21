from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\students.json"

with open(path) as f:
    data=load(f)
print(len(data))
# print(len(data))
# print([st.get("name")for st in data]) 