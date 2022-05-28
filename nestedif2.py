age=int(input("enter age"))
sex=input("enter sex")
if sex=="male":
    if age>=20 and age<=40:
        print("work anywhere")
    elif age>=40 and age<=60:
        print("urban")
    else:
        print("error")    
elif sex=="female":
    print("urban only")
else:
    print("ERROR")