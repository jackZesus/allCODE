total = 0
a  = 0.00

while True:
    val = input('enter the value > ' )
    if val == 'exit' or 'EXIT':
        break 
    try:
        val1 = float(val)
    except:
        print("invalid")
        continue
    total = total + 1
    a = a + val1


print("total number",total)
print("num",a)
print ("average", total /a)
