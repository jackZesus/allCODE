Mydict = {
    "apple": "wine",
    "cigar": "cuban",
    "winston": "churchuil",
    "leo": "tolstoy",
    "copydict": {"welcome": "indian"},
    "ar": [12, 34, 66, 67]
}
print(list[Mydict])
print(Mydict["winston"])
print(Mydict["copydict"]["welcome"])
Mydict["ar"] = [12, 45, 66]
print(Mydict["ar"])

dict3 = {
    "apple": "wine",
    "cigar": "cuban",
    "winston": "churchuil",
    "leo": "tolstoy",
    "copydict": {"welcome": "indian"},
    "ar": [12, 34, 66, 67]
}

copy = {
    "a": "ball",
    "b": "catch"
}
dict3.update(copy)
print(list(dict3))
print(list(tuple(dict3.keys())))
