import tkinter as tk
import tkinter.ttk as ttk


class App:
    """Define the application class."""
    def __init__(self):

        self.root = tk.Tk()
        self.label = tk.Label(self.root, text='hello world!', font='Arial 24')
        self.label.grid()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()


class Menu(tk.Menu):
    """Add a Menu() node to which a menu Item() can be attached."""
    def __init__(self, label, id=0, **kwargs):
        super(Menu, self).__init__(App.menus[0], **kwargs)
        App.menus[id].add_cascade(menu=self, label=label)
        App.menus.append(self)


# App().run()
