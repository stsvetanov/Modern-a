from functools import reduce
import time
a=lambda x: x+1
l=list(range(1000000))
t_1=time.process_time()
print(list(map(a,l)))
t_2=time.process_time()

for i in range(len(l)):
    l[i]+=1
print(l)
t_3=time.process_time()
delta_map=t_2-t_1
delta_for=t_3-t_2

delta=round(delta_map/delta_for,4)
if delta<1:
    print("Времето за map e по-добро с: %d" %(delta))
else:
    print("Времето за for e с: %d" %(delta))