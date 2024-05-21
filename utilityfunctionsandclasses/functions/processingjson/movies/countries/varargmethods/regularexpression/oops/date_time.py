def capitalize(fn):
    def wrapper():
        res=fn() #res=good morning
        res=res.upper()
        return res
    return wrapper

from datetime import datetime
# current_time=datetime.now()
# current_hours=current_time.hour
# print(current_hours)

@capitalize
def greetings_bytime():
    current_time=datetime.now()
    current_hours=current_time.hour
    if(5<current_hours<12):
        #print("good morning")
        return "good morning"
    elif(12<current_hours<18):
        #print("good afternoon")
        return "good afternoon"

    else:
        #print("good evening")
        return "good evening"

greetings_bytime()
print(greetings_bytime())
