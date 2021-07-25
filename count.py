#Write a Python program to count the number 4 in a given list.
a = int(input("ENTER THE NUMBER:- "))
b = int(input("ENTER THE NUMBER:- "))
c = int(input("ENTER THE NUMBER:- "))
d = int(input("ENTER THE NUMBER:- "))


List1 = [a, b, c, d,]
count = 0
for i in List1:
    if i == 12:
        count = count + 1

print(count)
