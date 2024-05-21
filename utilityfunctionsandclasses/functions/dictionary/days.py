lst=[ i for i in range(1,8)]
print(lst)

# 0 or 6 holiday else weekday

map_days=["holiday" if i in(1,7) else "weekday" for i in lst ]
print(map_days)
