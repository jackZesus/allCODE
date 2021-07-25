# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
a = (input("Enter the number to check: "))

try:
    if int(a) < 100:
        print("under 100")
    elif int(a) < 1000:
        print("under 1000")
    elif int(a) > 1000:
        print("above 10000", a)
except:
    print("invalid input Please check ", a)
    print("your input is mention above")
