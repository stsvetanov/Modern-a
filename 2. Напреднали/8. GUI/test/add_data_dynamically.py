# https://stackoverflow.com/questions/62747762/adding-data-dynamically-to-tkinter-table

from tkinter import ttk
import tkinter as tk


class InputData:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


def rest_call():
    return InputData("Ivan", "M", 32)


treev = None
window = None


def generate_data():
    # This is my API which makes a rest call and gets data
    api_data = rest_call()
    insert_data_dynamic(api_data)
    window.after(300, generate_data)


def insert_data_dynamic(api_data):
    treev.insert("", 'end', text="L1",
                 values=(api_data.name, api_data.gender, api_data.age))


if __name__ == "__main__":
    window = tk.Tk()
    window.resizable(width=1, height=1)
    treev = ttk.Treeview(window, selectmode='browse')
    treev.pack(side='right')

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(window,
                               orient="vertical",
                               command=treev.yview)

    # Calling pack method w.r.to verical
    # scrollbar
    verscrlbar.pack(side='right', fill='x')

    # Configuring treeview
    treev.configure(xscrollcommand=verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=500, anchor='c')
    treev.column("2", width=500, anchor='se')
    treev.column("3", width=500, anchor='se')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="Name")
    treev.heading("2", text="Sex")
    treev.heading("3", text="Age")
    generate_data()
    window.mainloop()