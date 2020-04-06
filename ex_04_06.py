def computepay(h,r):
        if h > 40:
            reg_pay = h * r
            ot_pay = (h-40.0) * (r * 0.5)
            pay = reg_pay + ot_pay
        else:
            pay = h * r
        return pay
help(round)
round(45.345,2)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hr = float(hrs)
rt = float(rate)
p = computepay(hr,rt)
print("Pay",p)

n = 100
while n > 0:
        print(n)
        n = n - 1
        print("test")
        print("test again")
        if n == 55:
                break
print(g,"day off")
