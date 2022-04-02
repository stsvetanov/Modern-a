# 40*10 + 5*15 = 475
WORK_HOURS = 40

rate = 10
hours = 45


def computepay(hours, rate=10):
    overtime = WORK_HOURS - hours
    if overtime < 0:
        return rate * hours
    else:
        return WORK_HOURS*rate + overtime*(rate*1.5)


print(computepay(rate,hours))
