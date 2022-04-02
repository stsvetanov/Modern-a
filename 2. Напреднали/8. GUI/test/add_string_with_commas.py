import tkinter as tk
from tkinter import ttk
app = tk.Tk()
tree = ttk.Treeview(app)
tree.grid(row=0, column=0)
tree.config(columns=('Value1'), selectmode='browse')
tree.column('#0', width=150, minwidth=10, stretch=tk.YES)
tree.column('Value1', width=80, minwidth=10, stretch=tk.YES)
tree.heading('#0', text='Name', anchor=tk.W)
tree.heading('Value1', text='Value', anchor=tk.W)
data = [['John', '123456'], ['Mary', '123 456'], ['Edward', 'abcdef'], ['Lisa', 'ab cd ef']]
for item in data:
    print(item[1], type(item[1]))
    tree.insert("", 'end', item[0], text=item[0], values=item[1])
    print(tree.item(item[0])['values'], type(tree.item(item[0])['values']))
app.mainloop()