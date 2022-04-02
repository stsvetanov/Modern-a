# Ако една цифра е по-голяма или равна на следващата тя се прибавя към общата стойност. В обратния случай се изважда.
# Да се напише клас roman_numbers, на който се подава стринг, представляващ римско число
# класът разполага с два атрибута: roman_number=на подадения стринг и arabic_number, който по подразбиране е 0
# да се напишат __init__ и __repr__ методите
# да се напише метод roman_arabic, който променя стойността на атрибута arabic_number с арабския му запис
# група 1: add_roman => връща сумат

class roman_arab_numbers:
    def __init__(self,roman_number="",arabic_number=0):
        self.rn=roman_number
        self.an=arabic_number
    def roman_arabic(self):
        D={"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500 ,"M":1000}
        arabicn=0
        for i in range(1,len(self.rn)):
            a=D[self.rn[i-1]]
            b=D[self.rn[i]]
            if a>=b: arabicn+=a
            else: arabicn-=a
        arabicn+=D[self.rn[-1]]
        self.an=arabicn
        return arabicn
    def arr_1(self,k=1):
        # за последната цифра
        D = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        s=""
        if int(k) < 4:
            s += D[1] * int(k)
        elif int(k) == 4:
            s += D[1] + D[5]
        elif int(k) > 4 and int(k) < 9:
            s += D[5] + D[1] * (int(k) - 5)
        else:
            s += D[1] + D[10]
        return s
    def arr_2(self,k=10):
        # за втора цифра от дясно на ляво
        D = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        s = ""
        if int(k) < 4:
            s += D[10] * int(k)
        elif int(k) == 4:
            s += D[10] + D[50]
        else:
            s += D[50] + D[10] * (int(k) - 5)
        return s
    def arr_3(self,k=100):
        # за трета цифра от дясно на ляво
        D = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        s = ""
        if int(k) < 4:
            s += D[100] * int(k)
        elif int(k) == 4:
            s += D[100] + D[500]
        else:
            s += D[500] + D[100] * (int(k) - 5)
        return s
    def arabic_roman(self):
        # най-голямото число за конвертиране е 3999
        D = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        le=len(str(self.an))
        s=""
        if le==4:
           s+=D[1000]*int(str(self.an)[0])
           s+=self.arr_3(str(self.an)[1])
           s += self.arr_2(str(self.an)[2])
           s += self.arr_1(str(self.an)[3])
        elif le==3:
            s += self.arr_3(str(self.an)[0])
            s += self.arr_2(str(self.an)[1])
            s += self.arr_1(str(self.an)[2])
        elif le==2:
            s += self.arr_2(str(self.an)[0])
            s += self.arr_1(str(self.an)[1])
        elif le==1:
            s += self.arr_1(str(self.an)[0])
        else: s="Error"
        self.rn=s
        return s
    def __repr__(self):
        if self.an==0: self.roman_arabic()
        if self.rn=="": self.arabic_roman()
        ss="Римски запис: %s\n" %(self.rn)
        ss += "Арабски запис: %s\n" % (self.an)
        ss += "_____________________\n"
        return ss

a=roman_arab_numbers(arabic_number=1)
print(a)

a=roman_arab_numbers(arabic_number=8)
print(a)
a=roman_arab_numbers(arabic_number=9)
print(a)
a=roman_arab_numbers(arabic_number=10)
print(a)

