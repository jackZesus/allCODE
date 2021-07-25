# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

first1 = int(input("Enter the First NUMBER :_ "))
if first1 >= 17:
    n = first1 - 17
    print("this is the double diff ", n*2)
else:
    print("number is lowe than 17 difference", 17 - first1)
