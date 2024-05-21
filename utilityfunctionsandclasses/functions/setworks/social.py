all_users=["mammotty","mohanlal","prithvi","asif","dq","fahad","nivin"]

nivin_frnds=["asif","dq","fahad"]

dq_frnds=["mammotty","asif","fahad","mohanlal"]


#nivin_suggestions

all_users_set=set(all_users)
nivin_frnds_set=set(nivin_frnds)
suggestions=all_users_set.difference(nivin_frnds)

suggestions.discard("nivin")
print(suggestions)

#to find mutual frnds of dq and nivin
mutual_frnds=nivin_frnds_set.intersection(dq_frnds)
print(mutual_frnds)
