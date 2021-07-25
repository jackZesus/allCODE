myDict = {
    "fast": "in a quick",
    "harry": "a corder",
    "anotherdic": {'harry': 'player'},
    "marks": [1, 2, 4, 5, 7]
}
print(myDict['anotherdic']['harry'])  # nested disct


# updation of value
myDict["marks"] = [25, 67]
print(myDict['marks'])
