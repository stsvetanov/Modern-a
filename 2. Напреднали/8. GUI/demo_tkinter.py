# There are two main methods - Tk and mainloop
# mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event
# import tkinter
# m = tkinter.Tk()
# '''
# widgets are added here
# '''
# m.mainloop()

# Button
# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()

# Задача: При натискане на бутона да се появи нов бутон, а когато новият е натиснат да затваря прозореца.
# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
#
#
# def create_button():
#     button2 = tk.Button(r, text='Stop', width=25, command=r.destroy)
#     button2.pack
#
#
# button = tk.Button(r, text='Next', width=25, command=create_button)
# button.pack()
# r.mainloop()


# from tkinter import *
#
# root = Tk()
# root.geometry('200x200')
# def CreateBt():
#     bt2 = Button(root, text='exit',  command=root.destroy)
#     bt2.pack()
#
# bt = Button(root,text='Button', command = CreateBt)
# bt.pack()
#
#
# root.mainloop()


# Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets.
# from tkinter import *
# master = Tk()
# w = Canvas(master, width=250, height=250)
# w.pack()
# canvas_height = 200
# canvas_width = 200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y)
# w.create_rectangle(20, 20, 50, 50)
# mainloop()

# # Създайте прозорец, в който да се визуализират 20 случайно генерирани точки с координати x и y.
# import random
# from tkinter import *
#
#
# def create_circle(x, y, r, canvasName): #center coordinates, radius
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvasName.create_oval(x0, y0, x1, y1)
#
#
# data = [(random.randint(1, 200), random.randint(1, 200)) for _ in range(20)]
#
# master = Tk()
# w = Canvas(master, width=250, height=250)
# w.pack()
# canvas_height = 200
# canvas_width = 200
#
# for el in data:
#     create_circle(el[0], el[1], 3, w)
#
# master.mainloop()

# It is used to input the single line text entry from the user.
# from tkinter import *
# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()


# # Listbox: It offers a list to the user from which the user can accept any number of options.
# import time
# from tkinter import *
#
# top = Tk()
# Lb = Listbox(top)
#
# my_list = ['Python', 'Java', 'C', 'Other']
#
#
# for index, item in enumerate(my_list):
#     number = index + 1
#     Lb.insert(number, item)
#     time.sleep(1)
#
# # Lb.insert(1, 'Python')
# # Lb.insert(2, 'Java')
# # Lb.insert(3, 'C++')
# # Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()


# from tkinter import *
#
# root = Tk()
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
# mainloop()

# from tkinter import *
# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, 'This is line number' + str(line))
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
# mainloop()

# import tkinter
#
# window = tkinter.Tk()
# window.title("GUI")
#
# # creating a function called say_hi()
# def say_hi():
#     tkinter.Label(window, text = "Hi").pack()
#
# tkinter.Button(window, text = "Click Me!", command = say_hi).pack() # 'command' is executed when you click the button
#                                                                     # in this above case we're calling the function 'say_hi'.
# window.mainloop()

import tkinter

def delete_line():
    canvas.delete(line1)


def create_line():
    line1 = canvas.create_line(25, 25, 250, 150)


window = tkinter.Tk()
window.title("GUI")

button_1 = tkinter.Button(window, text="Delete line!", command=delete_line).pack()
button_2 = tkinter.Button(window, text="Create line!", command=create_line).pack()

# creating the 'Canvas' area of width and height 500px
canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()

# 'create_line' is used to create a line. Parameters:- (starting x-point, starting y-point, ending x-point, ending y-point)
line1 = canvas.create_line(25, 25, 250, 150)
# parameter:- (fill = color_name)
line2 = canvas.create_line(25, 250, 250, 150, fill = "red")

# 'create_rectangle' is used to create rectangle. Parameters:- (starting x-point, starting y-point, width, height, fill)
# starting point the coordinates of top-left point of rectangle
rect = canvas.create_rectangle(500, 25, 175, 75, fill = "green")

# you 'delete' shapes using delete method passing the name of the variable as parameter.
# canvas.delete(line1)
# you 'delete' all the shapes by passing 'ALL' as parameter to the 'delete' method
# canvas.delete(tkinter.ALL)

window.mainloop()
