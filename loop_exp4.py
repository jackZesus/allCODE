''' filtering   in a loop
for i in [1,2,3,4,5,6,7,8,9]:
    if i > 5:
        print("greater than 20 ",i) '''

# SEARCHING THE NUMBER 

'''for i in  [1,2,3,4,5,6,7,8,9]:
    if i == 3:
        print("present in the list",i)
    elif i!=3:
        print(i)'''
        
# SMALLEST NUMBER IN LIST 
small = None
for i in [1,2,3,4,5,6,7,8,9]:
    if small is None:
         small = i
    elif i < small:
        small = 1 
print ("smallest value is ",small)


       
        