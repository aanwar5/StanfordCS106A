#Pay Wage Calculator
def computepay(hours, rate):
    print("In computepay", hours, rate)
    if fh > 40:
        # print("Overtime")
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        # print(reg, otp)
        pay = reg + otp
    else:
        # print("Regular Rate")
        pay = hours * rate
    print("Pay", pay)
    return pay


sh = input("Enter Hours: ") #string hours
sr = input("Enter Rate: ") #string rate
#printing (fh, fr)
fh = float(sh) #creating a float
fr = float(sr) #creating a float

xp = computepay(fh,fr)

