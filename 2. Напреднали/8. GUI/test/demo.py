from random import randint
from tkinter import *
from tkinter.ttk import Treeview


def get_window():
    root = Tk()
    root.resizable(width=True, height=True)
    root.geometry("823x458")
    root.title("PsControl")
    return root


def get_top_frame(root):
    frame = Frame(root)
    frame.name = 'top_frame'

    frame.root = root

    frame.pack(side=TOP, expand=False, fill=X)

    button1 = Button(frame, text="Add Row", command=lambda: tv.insert('', 'end', text="hostname"))
    button1.grid(row=0, column=1)

    button1 = Button(frame, text="Add Cow 1", command=lambda: tv_insert("H1", randint(1, 100)))
    button1.grid(row=0, column=2)

    button2 = Button(frame, text="Add Cow 2", command=lambda: tv_insert("H2", randint(1, 100)))
    button2.grid(row=0, column=3)

    button3 = Button(frame, text="Add Cow 3", command=lambda: tv_insert("H3", randint(1, 100)))
    button3.grid(row=0, column=4)

    button4 = Button(frame, text="Add Cow 20", command=lambda: tv_insert("H4", randint(1, 100)))
    button4.grid(row=0, column=5)

    button5 = Button(frame, text="Delete row", command=lambda: tv.delete(tv.selection()))
    button5.grid(row=0, column=6)


def get_bottom_frame(root):
    global tv
    frame = Frame(root, highlightbackground='#3E4149', highlightthickness=1, borderwidth=2)
    frame.name = 'bottom_frame'
    frame.root = root

    h = Scrollbar(root, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(root)
    v.pack(side=RIGHT, fill=Y)

    frame.pack(side=BOTTOM, expand=True, fill=BOTH)
    frame.config(background='#FFFFFF')

    tv = Treeview(frame, xscrollcommand=h.set, yscrollcommand=v.set)

    tv.column("#0", width=135, minwidth=35, stretch=NO)
    tv.heading("#0", text='Host', anchor='w')

    tv.pack(expand=True, fill='both')

    h.config(command=tv.xview)
    v.config(command=tv.yview)


def tv_insert(heading, insert_data):
    selection = tv.selection()
    columns = tv["columns"]
    if columns == '':  # if no columns, create column, heading and item.
        tv["columns"] = (heading,)
        tv.column(heading, width=135, minwidth=35, stretch=NO)
        tv.heading(heading, text=heading, anchor='w')
        tv.item(selection, values=(insert_data,))
    else:
        headings = [tv.heading(col) for col in columns] # save current headings

        if heading not in columns:
            new_col = columns + (heading,)
            tv["columns"] = new_col
            # restore previous headings
            for h in headings:
                tv.heading(h['text'], text=h['text'], anchor=h['anchor'])
            # set new heading
            tv.heading(heading, text=heading, anchor='w')
            # add data/item with with size of the columns
            data = tv.item(selection, "values")
            if data == '':
                len_col = len(new_col)
                new_data = ['' for _ in range(len_col)]            # Create an empty list
                new_data[len_col - 1] = insert_data                # Update the next
                tv.item(selection, values=tuple(new_data))
            else:
                new_data = data + (insert_data,)
                tv.item(selection, values=tuple(new_data))

        else:
            data = tv.item(selection, "values")
            # if heading exist but no item on the the selected row
            if data == '':
                data = ['' for _ in range(len(headings))]
                index = columns.index(heading)
                data[index] = insert_data
                tv.item(selection, values=tuple(data))
            else:
                data = list(data)
                if len(data) < len(columns):
                    new_data = ['' for _ in range(len(columns))]
                    for i, d in enumerate(data):
                        new_data[i] = d
                    index = columns.index(heading)
                    new_data[index] = insert_data
                    tv.item(selection, values=tuple(new_data))
                else:
                    index = columns.index(heading)
                    data[index] = insert_data
                    tv.item(selection, values=tuple(data))


def delete_row():
    selection = tv.selection()
    tv.delete(selection)


root = get_window()
get_top_frame(root)
get_bottom_frame(root)

root.mainloop()
