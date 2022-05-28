a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a+b>c:
    print("valid")
elif b+c>a:
    print("valid")
elif a+c>b:
    print("valid")
else:
    print("not valid")             