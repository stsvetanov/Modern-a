# A-Z [65;90]
# a-z [97;122]
# 0-9 [48;57]
# А-Я [1040;1065]
# а-я [1072;1097]
# ord('б')-ord('b')=975
# ord('Б')-ord('B')=975


AZ=''.join([chr(i)for i in range(ord('A'),ord('Z')+1)])
# fromm=ord('A')
# това е числото, което съответства на латинската буква А
# too=ord('Z')+1
# това е числото, което съответства на латинската буква Z +1
# AZ=[chr(i)for i in range(fromm,to)]
# генерираме списък от буквите
# AZ=''.join(AZ)
# слепваме всички букви от списъка, като резултатът е стринг

az=''.join([chr(i)for i in range(ord('a'),ord('z')+1)])
num=[chr(i)for i in range(ord('0'),ord('9')+1)]
num.append('@')#добавя го в края на списъка
num.append('!')#добавя го в края на списъка
num=''.join(num)
numcod=''.join(['о','и','д','е','ч','п','ш','т','ъ','щ','а','л'])
BG=''.join([chr(i)for i in range(ord('А'),ord('Я')+1)])
BG=BG[:26]
bg=''.join([chr(i)for i in range(ord('а'),ord('я')+1)])
bg=bg[:26]

str=input('Please input password, written in latin alphabet and digits:')
newpass=''

# зад.2 а)
for si in str:
          k_BG=BG.find(si)
          k_bg=bg.find(si)
          k_numcod=numcod.find(si)
          if k_numcod!=-1:
              str=str.replace(si,num[k_numcod])
              #newpass+=BG[k_AZ]
          elif k_bg!=-1:
              str=str.replace(si,az[k_bg])
              #newpass+=bg[k_az]
          
          elif k_BG!=-1:
              str=str.replace(si,AZ[k_BG])
              #newpass+=numcod[k_num]
          else: str=str.replace(si,"#")
        
# зад.2 б)
for i in range(0,len(str)):
    cond_1=(i+1)%3==0
    cond_2=str[i] in az
    if cond_1 & cond_2:
        str=str.replace(str[i],str[i].upper())
    
print("The new password is: "+str)
#print("The new password is: "+newpass)
