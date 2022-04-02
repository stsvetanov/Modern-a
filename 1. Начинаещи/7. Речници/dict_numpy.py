s='Ваканцията наплижава'
t='наближава'
# s[2:15]='канцията набли'
# for i in range(len(t)):
#     if t[:i+1] in s[2:15]:
#         print(t[:i+1],': ',s[2:15].find(t[:i+1]))
# print('END')

import numpy as np
n=np.zeros((len(s),len(t)),dtype=int)
# np.zeros(shape,dtype): shape=(брой редове, брой колони)

for r in range(len(s)):
    for c in range(len(t)):
        if s[r]==t[c]:
            n[r,c]=1
print(n)
d=dict() # празен речник
dd=dict()
br=len(s)-len(s)%len(t)
for b in range(br):
    print(b)
    # d[b]=sum(n[b:b+len(t),::].diagonal())
    dd[sum(n[b:b+len(t),::].diagonal())]=b
#     речникът dd е със формат „брой съвпадения по диагонал“:пореден номер на матрицата
#     когато броят на съвпаденията се повтаря, в речника ще остане последната изчислена стойност
#     n[b:b+len(t),::] представлява квадратна матрица
#     с брой редове, колкото са символите в по-късия стринг


maxsymb=max(dd.keys()) # намира най-големия ключ, т.е. най-голямото съвпадение
mybr=dd[maxsymb] # намира номера на матрицата за най-голямото съвпадение
print('номер на матрицата с най-голямо съвпадение: %d'%(mybr))
print('максимален брой символи на съвпадение: %d'%(maxsymb))
# print(mybr)
mymat=n[mybr:mybr+len(t),::].diagonal()
# mymat е диагонала на матрицата с най-голямо съвпадение
newS=''
for i in range(len(t)):
    # натрупваме в newS символите, които участват в най-голямото съвпадение
    if mymat[i]==1:newS+=t[i]
    else: newS+='_'
print(newS)


sum()
