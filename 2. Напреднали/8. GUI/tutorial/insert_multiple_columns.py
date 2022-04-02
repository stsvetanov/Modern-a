"""Insert multiple columns to the tree."""

from tkinter import *

root = Tk()

root.resizable(width=True, height=True)
root.geometry("823x458")
root.iconbitmap('icos/icon.ico')
root.title("PsControl")

# tk.Label('Columns', font='Arial 24')

tree = Treeview()
tree['columns'] = ('size', 'date', 'type')
tree['columns'] = range(3)

text = tk.Entry('Text', 'print(self.val.get())')
row = tk.Spinbox('Row:', 'print(self.val.get())', to=100)
col = tk.Spinbox('Column:', 'print(self.val.get())', to=100)
tk.Button('Set', 'App.tree.set(App.tree.focus(), App.col.val.get(), App.text.get())')

for i in range(2):
    tree.column(i, width=100, anchor='w')
    tree.heading(i, text='Heading' + str(i))

    L = 'Hello;Dolly;How;Are;You'.split(';')
    for item in L:
        tree.insert('', 'end', text=item)

root.mainloop()
