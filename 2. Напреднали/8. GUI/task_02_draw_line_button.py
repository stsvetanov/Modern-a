import tkinter


def draw_line():
    global line1
    line1 = canvas.create_line(25, 25, 250, 150)


def delete_line():
    canvas.delete(line1)


window = tkinter.Tk()
window.title("GUI")
canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

tkinter.Button(window, text="Draw Line", command=draw_line).pack()
tkinter.Button(window, text="Delete line", command=delete_line).pack()

rect = canvas.create_rectangle(500, 25, 175, 75, fill="green")

window.mainloop()