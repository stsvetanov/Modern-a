import numpy as np
import random as rd
rows=5
cols=10
L=[rd.randint(1,100) for i in range(20)]
shape=(5,4)
mat=np.array(L).reshape(shape)
print(mat)

# 13. Напишете Python програма, за да създадете 2D масив, в който сумите по колони са еднакви
print("Task 13")
diff_bycol=max(mat.sum(axis=0))-mat.sum(axis=0) # разликите между максималната сума и сумите по колони за всяка колона
print(mat.sum(axis=0))
print(diff_bycol)
mat[0,:]=mat[0,:]+diff_bycol
print(mat)
print(mat.sum(axis=0))


# 14. Напишете Python програма, за да създадете 2D масив, в който сумите по редове са еднакви
print("Task 14")
diff_byraw=max(mat.sum(axis=1))-mat.sum(axis=1) # разликите между максималната сума и сумите по колони за всяка колона
print(mat.sum(axis=1))
print(diff_byraw)
mat[:,0]=mat[:,0]+diff_byraw
print(mat)
print(mat.sum(axis=1))

# 15. Напишете Python програма, за да създадете 2D масив, в който произведенията по колони са еднакви
print("Task 15")
def pro(mat, axis=0):
    # axis=0, пресмята по произведението на елементите по колони
    # axis=1, пресмята по произведението на елементите по редове
    pro=[]
    if axis==0:
        for i in range(np.shape(mat)[1]):
            k=1
            for j in range(np.shape(mat)[0]):
                k*=mat[j,i]
            pro.append(k)
    elif axis==1:
        for i in range(np.shape(mat)[0]):
            k=1
            for j in range(np.shape(mat)[1]):
                k*=mat[i,j]
            pro.append(k)
    else: pro=0
    return pro
L=[rd.randint(1,5) for i in range(20)]
shape=(5,4)
mat=np.array(L,dtype=float).reshape(shape)
print(mat)
proiz=pro(mat)
diff_bycol=max(proiz)/proiz # разликите като множители по колони за всяка колона
print(proiz)
print(diff_bycol)
mat[0,:]=mat[0,:]*diff_bycol
print(mat)
print(pro(mat))
# 16. Напишете Python програма, за да създадете 2D масив, в който произведенията по редове са еднакви
print("Task 16")
L=[rd.randint(1,5) for i in range(20)]
shape=(5,4)
mat=np.array(L,dtype=float).reshape(shape)
print(mat)
proiz=pro(mat,1)
diff_byraw=max(proiz)/proiz # разликите като множители по колони за всяка колона
print(proiz)
print(diff_byraw)
mat[:,0]=mat[:,0]*diff_byraw
print(mat)
print(pro(mat))
# 17. Напишете Python програма, за да създадете 2D масив, в който сумите по колони се увеличават монотонно с нарастването на номера на колоната
print("Task 17")
# същото е като задача 21

# 18. Напишете Python програма, за да създадете 2D масив, в който произведението по редове е монотонно увеличаващ се с нарастването на номера на колоната
# използваме функцията pro=proiz(mat), резултатът са произведенията по редове
# ind_sort_ind=np.argsort(pro)
# mat=mat[ind_sort_ind,:] # подреждаме матрицата
# модифицираме матрицата

# 19. Напишете Python програма, за да създадете 2D масив, в който сумите по колоните се намаляват монотонно с нарастването на номера на колоната
# поп подобие на зад.21, но:
# ind_sort_ind=np.argsort(sums_bycol)
# ind_sort_ind=ind_sort_ind=[::-1] # обръща реда на идексите

# 20. Напишете Python програма, за да създадете 2D масив, в който произведението по редове е монотонно намаляващо се с нарастването на номера на колоната
# използваме функцията pro=proiz(mat,1), резултатът са произведенията по редове
# ind_sort_ind=np.argsort(pro)
# ind_sort_ind=ind_sort_ind=[::-1]
# mat=mat[ind_sort_ind,:] # подреждаме матрицата
# модифицираме матрицата

# 21. Напишете Python програма, за да създадете 2D масив. Намерете сумите по колони и пренаредете колоните в масива, така че ако сумата на елементите в колона 1 > сумата на елементите в колона 2 => то двете колони да си разменят поредността в масива
print("Task 21")
# >>>A.sum(axis=0)  - сума по колони
# >>>A.sum(axis=1)  - сума по редове
sums_bycol=mat.sum(axis=0)
print(sums_bycol)
ind_sort_ind=np.argsort(sums_bycol)
print(ind_sort_ind)
new_mat=mat[:,ind_sort_ind]
print(new_mat)