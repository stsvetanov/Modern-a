s='Баба Марта ми донесе много мартенички'
# стрингът s има 37 символа
# първият символ от стринга винаги е с индекс 0
# последният символ от стринга=len(s)-1
newS=''
for i in range(len(s)):
    # i е поредният индекс на символ от стринга
    # range(от=0,до,стъпка=1) =>[от;до)
    if s[i]=='а': newS+='@'
    else: newS+=s[i]
print(newS)

s=newS
newS=''
for i in range(1,len(s),2):
    # i е поредният индекс на символ от стринга
    # range(от=0,до,стъпка=1) =>[от;до)
    newS+=s[i-1]+'!'
print(newS)

print(newS.find('!н!'))
print('@: '+str(newS.count('@')))
print('!: '+str(newS.count('!')))
print('*: '+str(len(newS)-newS.count('@')-newS.count('!')))

