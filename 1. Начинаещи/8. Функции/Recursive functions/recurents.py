def rec_01(a1,n):
    if n<=0: return 5/4
    elif n==1: return a1
    else: return 4*(rec_01(a1,n-1)-rec_01(a1, n-2))

def rec_02(a1,n):
    if n<=2: return a1
    else: return 2**(n-1)-rec_02(a1,n-1)

def rec_03(a1,n):
    if n<1000:
        if n<=1: return a1
        else: return rec_03(a1,n-1)
    else: return rec_03(a1,10)

def rec_04(a1,n):
    if n<=0: return 2
    elif n==1: return a1
    else: return 2*rec_04(a1,n-1)-rec_04(a1,n-2)

# def rec_05(a1,n):
#     global dic
#     if n<2: return dic
#     else:
#         if n not in dic:
#             val=2*rec_05(a1,n-1)-rec_05(a1,n-2)
#             dic.update({n:val})

# Примери за използване на функциите:
print(rec_01(3,7))
print([rec_02(1, x) for x in range(1,12)])
print(rec_03(137,8999))
print([rec_04(4,x) for x in range(1,16)])
dic={0:2,1:4}
print(rec_05(dic[1],10))
print(dic)