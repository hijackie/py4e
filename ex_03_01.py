xh = input("Enter Hour: ")
xr = input("Enter Rate: ")
xh = float(xh)
xr = float(xr)

if xh > 40:
    plus = xh - 40
    xh = 40
pay = xh * xr + 1.5 * plus * xr
print (pay)
