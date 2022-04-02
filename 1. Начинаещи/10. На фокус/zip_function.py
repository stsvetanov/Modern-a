Lat_degrees=(0, 10 ,23.43, 30, 23.43, 66.57, 70, 66.57, 90,90)
Lat_pole=  ('S','S','N',   'N','S',   'S',   'N','N',  'N','S')
z=zip(Lat_degrees,Lat_pole)
for i in z:
    a,b=i
    print(a,b)

S,N=[],[]
for i in range(len(Lat_degrees)-1):
    cond=Lat_pole[i]=='S'
    if cond: S.append(Lat_degrees[i])
    else: N.append((Lat_degrees[i]))
print(S)
print(N)


