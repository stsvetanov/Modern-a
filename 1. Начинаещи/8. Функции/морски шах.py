import random
table = []
turn,victory,gametype,moves = 0,0,0,0

def init():
   for a in range(9):
      table.append(str(a+1))
#funkciq za stoinostite na poletata

def screen(table,turn):
   for a in range(3):
      for b in range(3):
         print(table[a*3+b],end = "  ")
         if b == 2:
            print("\n")
   if turn == 1:
      print("O e на ход")
   else:
      print("X e на ход")
   print("\n\n\n")


def screengameover(table):
   print("\n")
   for a in range(3):
      for b in range(3):
         print(table[a*3+b],end = "  ")
         if b == 2:
            print("\n")
   print("\n\n\n\n\n\n\n\n\n")
#funkciq za pokazvane na ekrana

def turns(turn):
   if turn == 0:
      return 1
   else:
      return 0
#funkciq za smqna na hodovete

def select(table,turn):
   inputt = int(input())
   if turn == 0:
      select = "X"
   else:
      select = "O"
   table[int(inputt)-1]=select
#funkciq za vuvejdane

def selectkomp(table,turn,inputt):
   if turn == 0:
      select = "X"
   else:
      select = "O"
   table[int(inputt)-1]=select
#funkciq za vuvejdane

def checker(table,turn):
   if moves != 9:

      if table[0] == table[1] == table[2] or table[3] == table[4] == table[5] or table[6] == table[7] == table[8] or table[0] == table[3] == table[6] or table[0] == table[4] == table[8] or table[1] == table[4] == table[7] or table[2] == table[5] == table[8] or table[2] == table[4] == table[6]:
            if turn == 1:
               return 1
            elif turn == 0:
               return 2

      else:
              return 0
   return 3
#funkciq za proverka

def gamesel(gametype): 
   print("За играч срещу играч,въведете 1","За играч срещу компютър,въведете 2",sep = "\n")
   while gametype != 1 and gametype != 2:
      gametype = int(input())
   if gametype == 1:
      rungamepvp(table,turn,victory)
   if gametype == 2:
      rungameendif1(table,turn,victory)
#funkciq za izbor na rejim



def pobeditel(victory):
   if victory == 1:
      print("X е победител!")
      screengameover(table)
   elif victory == 2:
      print("O е победител!")
      screengameover(table)
   elif victory == 3:
      print("Всички полета са запълнени.")
      screengameover(table)
      

#funkciq za pobeditel

def endif1(turn):
   global table
   filled=[table[i] for i in range(0,9) if table[i] not in ("X","O")]
   inputt = random.choice(filled)
   selectkomp(table,turn,inputt)

#funkciq za igra4 sre6tu komputr

def rungamepvp(table,turn,victory):
   while victory == 0:
       screen(table,turn)
       select(table,turn)
       turn =turns(turn)
       global moves
       moves+=1
       victory = checker(table,turn)
   pobeditel(victory)
#funkciq za igra4 sre6tu igra4

def rungameendif1(table,turn,victory):
   while victory == 0:
      if turn == 0:
         screen(table,turn)
         select(table,turn)
      else:
         endif1(turn)
      turn = turns(turn)
      global moves
      moves+=1
      victory = checker(table,turn)
   turn = turns(turn)
   pobeditel(victory)

#funkciq za 1va trudnost

init()
gamesel(gametype)





