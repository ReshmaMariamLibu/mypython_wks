# list comprehension

lst=[3,4,5,6,7,8,9]
#squares
squares=[num**2 for num in lst ]
print(squares)

#cubes
cubes=[num**3 for num in lst ]
print(cubes)

#add 2 numbers

add_2=[num+2 for num in lst]
print(add_2)

#even
evens=[num for num in lst if num%2==0]
print(evens)

#odds
odds=[num for num in lst if num%2!=0]
print(odds)