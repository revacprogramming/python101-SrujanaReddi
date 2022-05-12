# Conditional Execution

hrs = float(input("Enter hours? "))
rate = float(input("enter rate"))
if hrs<=40:
  pay = hrs*rate
else:
  pay = ((hrs-40)*rate*1.5)+ (40*rate)
print(pay)
