val = input("enter a number ")
try:
    i = int(val)
    print("conversion sucessful")
except:
    i = -1

if i > 0:
    print("the number is ",i)
else:
    print("nt a number")
