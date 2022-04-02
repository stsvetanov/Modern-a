hours = 10
rate = 10
#
#
# def computepay(hours, rate):
#     overtime = hours - 40
#     rate1 = rate * 0.5
#     if overtime < 0:
#         payment = (hours * rate)
#     else: payment = (hours * rate) + (overtime * rate1)
#     return payment
#
#
# print(computepay(hours, rate))

def computepay(hours, rate):
    overtime = hours - 40
    rate1 = rate * 0.5
    if overtime > 0:
        payment = (hours * rate) + (overtime * rate1)
    else: payment = (hours * rate)
    return payment

print (computepay(hours, rate))