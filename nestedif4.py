day=input("enter day")
meal_time=input("enter meal time")
if day=="monday":
    if meal_time=="lunch":
        print("sambhar rice")
    else:
        print("chicken")
elif day=="tuesday":
    if meal_time=="breakfast":
        print("poha")
    else:
        print("dal")
else:
    print("no food")                        