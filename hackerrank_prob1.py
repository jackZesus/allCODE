# LEAP YEAR PROGRAM

year = int(input("enter the year:- "))  # OUTPUT REC FORM USER
if year % 4 == 0:  # LOGIC
    if year % 400 == 0:
        print("True")
else:
    print("false")  # OUTPUT DELIVERED
