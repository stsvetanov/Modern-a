import time
def fibonacci(n):
   if n==0: return 0
   elif n==1: return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans
    return ans

d = {0:1,1:1, 2:2} # Задават се изключенията
t0 = time.process_time()
print(fib_efficient(6, d))
t1 = time.process_time() - t0
print("Числото на Фибоначи с позиция n="+str(7)+" e: "+str(fibonacci(7)))
t2= time.process_time() - t1
print("Рекурсията за поредното число на Фибоначи е "+str(t2//t1)+" пъти по-бавна от Рекурсията с речници")
print(d)
