while True:
    line = input('enter >')
    if line[0] == "#":
        continue
    if line == 'done':
        break
    print(line)

print("done")