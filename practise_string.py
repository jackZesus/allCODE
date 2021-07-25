'''a = input("enter your name ")
print('good after noon ' + a)''' 
# question no 1 







# question number 2 

letter = ''' dear <|name|>,
you are selected !
date: <|date|>
'''
name = input("enter the name\n ")
date = input("enter the date\n ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)


st ="this is double space   "
str1 = st.find("  ")
print(str1)