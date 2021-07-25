"There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value"


def rem(dvi, dvs):
    return dvi % dvs


dvi = int(input("enter the first no :- "))
dvs = int(input("enter the second no :- "))
print(rem(dvi, dvs))
