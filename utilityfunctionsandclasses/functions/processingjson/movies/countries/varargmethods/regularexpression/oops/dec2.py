def capitalize(fn):
    def wrapper():
        res=fn() #res=good morning
        res=res.upper()
        return res
    return wrapper

@capitalize
def morning_greetings():
    return "good morning"

@capitalize
def afternoon_greetings():
    return "good afternoon"

print(morning_greetings())
print(afternoon_greetings())


