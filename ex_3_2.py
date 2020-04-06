hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
print(h, r)
if h > 40:
    reg = h * r
    ot = (h-40.0) * (r * 1.5)
    pay = reg + ot

else:
    pay = h * r
print("Pay:",pay)
