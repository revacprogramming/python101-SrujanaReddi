# Functions


def computepay(hrs, rte):
  pay = (hrs-40)*rte*1.5+ 40*rte
  return pay

def main():
    hrs=float(input("Enter hours?"))
    rte=float(input("Enter rate per hour"))
    p = computepay(hrs,rte)
    print("Pay",p)

main()
