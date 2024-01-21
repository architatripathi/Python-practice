a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

c = a+b
d = a-b
e = a*b
f = a/b

h = input("Enter the type of operation you want to perform:")

if h == "+":
    print(c)
elif h == "-":
    print(d)
elif h == "*":
    print(e)
elif h == "/":
    print(f)
else:
    print("Enter the operation you want to perform in symbolic form")

