character=input("enter character")
digit=int(input("enter digit"))
if character>="A" and character<="Z" or character>="a" and character<="z":
    print("it's alphabet")
elif character>=0 and character<0:
    print("it's digit")
else:
    print("it's special character")    