# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def Copy(str, c):
    result = ""
    for i in range(c):
        result = result + str
        return result


print(Copy('for',2))


'''def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))'''
