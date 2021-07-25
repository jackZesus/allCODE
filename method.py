mydict = {
    "fast": "in a quick",
    "harry": "a coder",
    "anotherdic": {'harry': 'player'},
    "marks": [1, 2, 4, 5, 7]
}
# method
print(type(mydict.keys()))    # PRINT Keys in the
print(list(mydict.keys()))  # putting the keys in the list
print(mydict.values())  # print the value
print(mydict.items())  # print(key,value) for all  contains of the dict
print(mydict)
dict2 = {
    "love": "update",
    "divya": "update2",
    "harry": "programmer"
}
mydict.update(dict2)  # updating
print(mydict)  # printing the update

print(mydict.get("harry"))  # returns 0 if the key is nt there in the dict
print(mydict["harry"])  # retunrs  an error
