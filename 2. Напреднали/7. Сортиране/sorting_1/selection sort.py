A=[12,3,15,4,8,1.7,10]
print(A)
for i in range(len(A)):   
    # Намира най-малкия елемент в несортираната част от масива
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Размяна на на намерения най-малък елемент с поредния несортиран     	
    A[i], A[min_idx] = A[min_idx], A[i]
    print(A)
