"Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers."


def side_Edge(side1, side2):
    return (side1 + side2) - 1


side1 = int(input("ENTER THE Side1:- "))
side2 = int(input("ENTER THE Side2:- "))
print(side_Edge(side1, side2))
