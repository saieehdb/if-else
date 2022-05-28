a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a<b and b<c:
    print("b")
elif a<b and a>c:
    print("a")
elif a<c and c>b:
    print("c")
else:
    print("none")            