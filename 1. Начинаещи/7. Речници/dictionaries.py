grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
# Извличане на ключовете от даден речник като списък
k=[k[1] for k in enumerate(grades.keys())]
# k=list(grades.keys())
# Извличане на ключовете от даден речник като списък
b=[b[1] for b in enumerate(grades.values())]
# b=list(grades.values())
print(grades)
print(k)
print(b)
