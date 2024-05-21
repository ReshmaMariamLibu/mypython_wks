#"string"
#'string'
#""""string"""

# string =sequence of characters

# name="luminar Technolab"
# print(name.casefold()) -uppercase to lowercaSe
# print(name.casefold().count('l'))
# print(name.capitalize()) -first leeter to uppercase

# print(name.count('a'))

# print(name.startswith('lu'))

# print(name.endswith('lab'))
# print(name.isalpha()) #to take alphabet
name="1034hello"
print(name.isdigit()) #digit to string

print(name.isalnum())

name="hello,good,morning,all"
words=name.split(",")
for w in words:
    print(w)