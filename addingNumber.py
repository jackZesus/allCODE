# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
num1 = int(input("ENTER THE FIRST NUMBER:- "))
num2 = int(input("ENTER THE 2ND NUMBER:- "))
num3 = int(input("ENTER THE 3RD  NUMBER:- "))

if num1 == num2 and num1 == num3:
    print("HERE IS YOUR ANS ", num1+num2+num3)
else:
    print("input fail to match")
