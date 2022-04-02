# зад.2: Да се опише клас с метод, който по дадени естествени числа n и p намира
# и връща броят на цифрите в записа числото n в p-ична бройна система:

class NPnumber:
    def __init__(self,n=10,p=10):

        if isinstance(n,int): self.num=n
        else: self.num=10
        if isinstance(p,int) and p<=36: self.base=p
        else: self.base=10
        # Проверява дали инициализиращите стойности отговарят на критериите
        # Ако не отговарят обектът приема стойности по подразбиране
    def dec_to_base(self):  # Maximum base - 36
        base_num = ""
        while self.num > 0:
            dig = int(self.num % self.base)
            if dig < 10:
                base_num += str(dig)
            else:
                base_num += chr(ord('A') + dig - 10)  # Using uppercase letters
            self.num //= self.base
        base_num = base_num[::-1]  # To reverse the string
        return base_num

    def __repr__(self):
        s = self.dec_to_base()
        k=str(self.num)
        dig = []
        for i in range(len(s)):
            try:
                int(s[i])
                dig.append(1)
            except:
                dig.append(0)
        digits=str(sum(dig))
        s="("+k+",10)"+"=> ("+s+","+str(self.base)+") => има "+digits+" цифри в записа си."
        return s

# n = input("Въведете естествено число за 'n': ")
# p = input("Въведете естествено число <36 за 'p': ")

# print(NPnumber())
# print(NPnumber(n,p))
print(NPnumber(15610,16))