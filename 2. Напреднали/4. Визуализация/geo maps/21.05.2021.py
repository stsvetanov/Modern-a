import graphics as gp
p1 = gp.Point(50,60)
p2 = gp.Point(150,120)
l1=gp.Circle(p1,20)
L=[p1,p2,l1]
win = gp.GraphWin("УП",600,400)
# p1.draw(win)
# p2.draw(win)
# l1.draw(win)
# Алтернативно изчертаване:
l1.setFill("yellow")
l1.setOutline("red")
# p1.setWidth(4)
p1.setFill("blue")
p2.setFill("green")

for l in L:
    try: gp.Point.draw(l,win)
    except: gp.Circle(l,win)
    # Работим с Try/eXcept, защото в L имаме обекти от тези два класа
win.getMouse()
l1.setFill("red")
l1.setOutline("yellow")
# p1.setWidth(4)
p1.setFill("green")
p2.setFill("blue")
for l in L:
    # Прерисуваме обектите, като е необходимо първо да
    # изтрием обекта и след това отново да го нарисуваме
    l.undraw()
    l.draw(win)
win.getMouse()
x=list(range(10))
y=[-x for x in range(10)]
for i in range(10):

    p1.undraw()
    l1.undraw()
    # Посоката е надясно и надолу
    p1.x+=10
    p1.y+=10
    l1=gp.Circle(p1,20)
    # независмо, че центърът е подаден чрез обект, т.е. има указател
    # който би следвало да сочи към обекта и да взима текущатата му стойност
    # това тук не сработва и се налага отново създаване на обекта кръг !!!
    p1.draw(win)
    l1.draw(win)
    win.getMouse()
# Алтернативно придвижване с .move()
for i in range(10):
    p1.move(-10,-10)
    l1.move(-10,-10)
    # l1.setFill(color_rgb(179, 255, 184))
    win.getMouse()

clrs=gp.color_rgb(179, 255, 184)
l1.setFill(clrs)

drawtext=gp.Text(p2,"Начало на играта :)")
s=lambda x,y:round(x+y,2)
p=lambda x,y:round(x*y,2)
s1=lambda x,y:round(x-y,2)
d=lambda x,y:round(x/y,2)
operators={"+":s,"-":s1,"*":p,"/":d}
import random as rd
for i in range(5):
    x=rd.randint(0,10)
    y=rd.randint(0,10)
    o=list(operators.keys())[rd.randint(0,3)]
    result=operators[o]
    result=result(x,y)
    question="%d %s %d = ???" %(x,o,y)
    p2.y+=20
    qdraw=gp.Text(p2,question)
    qdraw.draw(win)
    center=gp.Point(p2.x,p2.y+40)
    input_box = gp.Entry(center, 20)
    input_box.setText("Отговор")
    input_box.draw(win)
    win.getMouse()
    user_input = float(input_box.getText())
    if result==user_input:
        endtext="Браво!"
    else: endtext="Опитай следващия път..."
    newpoint=gp.Point(p2.x,p2.y+70)
    qdraw = gp.Text(newpoint, endtext)
    qdraw.draw(win)



win.getMouse()
win.close()
