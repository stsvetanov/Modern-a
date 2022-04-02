#1. Създайте променливи от тип: integer, float, string, boolean
a=5
b=5.5
c="text"
d=True
print("a="+str(a))
print("Типът на a е: "+str(type(a)))
print("b="+str(b))
print("Типът на b е: "+str(type(b)))
print("c="+str(c))
print("Типът на c е: "+str(type(c)))
print("d="+str(d))
print("Типът на d е: "+str(type(d)))


#2. Опитайте да превърнете всяка една промелива в променлива от
#другите типове по-горе

print(int(b))
# print(int(c))    ValueError: invalid literal for int() with base 10: 'text'
#Стрингът не съдържа число и не може да бъде превърнат в тип intrger
print(int(d))
print(float(a))
# print(float(c))  ValueError: could not convert string to float: 'text'
#Стринг не може да се превърне в тип float
print(float(d)) 
print(str(a))
print(str(b))
print(str(d))
print(bool(a))
print(bool(b))
print(bool(c))



#4. Демонстрирайте различните оператори чрез променливите от т.1
print("a+b="+str(a+b))          #+
print("a-b="+str(a-b))          #-
print("a*b="+str(a*b))          #*
print("a**b="+str(a**b))        #**
print("a/b="+str(a/b))          #/
print("a//b="+str(a//b))        #//
print("a%b="+str(a%b))          #%
print("a==b  "+str(a==b))       #==
print("a!=b  "+str(a!=b))       #!=
print("a<b  "+str(a<b))         #<
print("a>b  "+str(a>b))         #>
print("a<=b  "+str(a<=b))       #<=
print("a>=b  "+str(a>=b))       #>=
print("d and c  "+str(d and c)) #and
print("d or c  "+str(d or c))   #or
print("not b  "+str(not b))     #not



#6. Намислете проста задача, която според вас е изпълнима чрез включения материал
#в лекцията: опишете условието и се опитайте да я решите.

#Условие - Въведете две числа и проверете дали и двете се делят на 5
x=int(input("Въведете цяло число: "))
y=int(input("Въведете цяло число: "))
if x%5==0 and y%5==0: print ("И двете числа се делят на 5")
elif  x%5==0 or y%5==0: print ("Поне едно от числата се дели на 5")
else: print ("Нито едно от числата не се дели на 5")


