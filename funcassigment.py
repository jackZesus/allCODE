ava1 = input('enter the day')
ava2 = input('enter the rate')

def totalpay(day,rate):
    pay = day * rate
    return pay

try:
    x = int(ava1)
    y = float(ava2)
    print("payout is ",totalpay(x,y))
except:
    print("INVALID input")