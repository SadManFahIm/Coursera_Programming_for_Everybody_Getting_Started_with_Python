hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate/hour:"))
overtime = 0

if(hrs > 40):
    overtime = hrs - 40
    
pay = ((hrs-overtime) * rate) + (overtime * rate * 1.5)
print (pay) 