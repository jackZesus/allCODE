a = int(input("enter a number 1:-  "))  # 1 2 3 4
b = int(input("enter a number 2:-  "))
c = int(input("enter a number 3:-  "))
d = int(input("enter a number 4:-  "))

print(a, b, c, d)

if (a > d):
    a1 = a
else:
    a1 = d

if (b > c):
    a2 = b
else:
    a2 = c

if a1 > a2:
    print(list(str(a1) + " is greater "))
else:
    print(list(str(a2) + " is greater"))
