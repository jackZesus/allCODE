'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.'''



salary = int(input("enter salary "))
yos = int(input("enter years of service ")) #input taken from the user 

if yos >= 5:
    bonus = salary * 0.05               # calculation done 
    print("your bonous ", bonus)
else :
    print("you are nt eligible for bonus")  # result printed