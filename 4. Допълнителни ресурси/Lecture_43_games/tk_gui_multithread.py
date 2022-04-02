import struct
import queue

from tkinter import *
from socket import *
# import Queue
import threading
import tkinter.scrolledtext as tkst

skt = socket(AF_INET, SOCK_STREAM)
skt.connect(("localhost", 6666))
root = Tk()


def main():
    thread = threading.Thread(target = recieve)

    thread.start()

    root.mainloop()

def start_func():
    m = 6

def create_func():
    m = 10

def change_func():
    m = 2
    print(m)

def fight_func():
    m = 3
    print(m)

def pvp_func():
    m = 4
    print(m)

def loot_func():
    m = "5"
    skt.send(m.encode())
    print(m)

def leave_func():
    m = 12
    print(m)

def submit_value():
    global userEntry
    length = len(userEntry.get())
    e1.delete(0, END)

class TestClient(Frame):
    def __init__(self, master):
        global userEntry
        Frame.__init__(self, master)
        self.pack()

        for n in range(3):
            self.grid_rowconfigure(n, weight=1)

        for n in range(8):
            self.grid_columnconfigure(n, weight=1)

        self.Messg_text = tkst.ScrolledText(self,wrap = WORD, width=80)
        self.Messg_text.grid(row=0, column=0, columnspan=8)

        la1 = Label(self, text="Value entry:")
        la1.grid(row=1, column=0)

        userEntry = StringVar()
        global e1
        e1 = Entry(self, width=40, textvariable=userEntry)
        e1.grid(row=1, column=1, columnspan=6)

        e2 = Button(self, text="Enter", command=submit_value)
        e1.delete(0, END)
        e2.grid(row=1, column=5, columnspan=10)


        b1 = Button(self, text="Start", width=10,padx=10,pady=10, command=start_func)
        b1.grid(row=2, column=0)

        b0 = Button(self, text="Create Character", width=10,padx=10,pady=10, command=create_func)
        b0.grid(row=2, column=1)

        b2 = Button(self, text="Change Room", width=10,padx=10,pady=10, command=change_func)
        b2.grid(row=2, column=3)

        b3 = Button(self, text="FIGHT", width=10,padx=10,pady=10, command=fight_func)
        b3.grid(row=2, column=4)

        b4 = Button(self, text="PvP FIGHT", width=10,padx=10,pady=10, command=pvp_func)
        b4.grid(row=2, column=5)

        b5 = Button(self, text="Loot", width=10,padx=10,pady=10, command=loot_func)
        b5.grid(row=2, column=6)

        b6 = Button(self, text="Leave", width=10,padx=10,pady=10, command=leave_func)
        b6.grid(row=2, column=7)

        #Data Queue
        self.queue = queue.Queue()
        self.queue_check()
    def queue_check(self):
        try:
            #Inserts Data
            text = self.queue.get_nowait()
            self.Messg_text.insert(INSERT, text)
        #If Nothing In Queue
        except queue.Empty:
            #Repeats Itself After 100 ms
            self.after(100, self.queue_check)

tw = TestClient(root)
def recieve():
    while(True):
        mesg_type = skt.recv(1)
        if(mesg_type == b'\x01'):
            msg_Len = skt.recv(2)
            msg_int_Len = struct.unpack('h',msg_Len)
            Recip_Name = skt.recv(32)
            sender_Name = skt.recv(32)
            mesg = skt.recv(msg_int_Len)
            PostMessage(Recip_Name,sender_Name,mesg)

        elif(mesg_type == b'\x0b'):
            init_Points = skt.recv(2)
            statLim = skt.recv(2)
            descriptLen = skt.recv(2)
            descriptLen = struct.unpack('h', descriptLen)
            gameDiscript = skt.recv(descriptLen[0])
            print(gameDiscript.decode("utf-8"))
            Post11Message(str(gameDiscript)[0:-2])


def PostMessage(name, senderName, Message):
    #Adds Message To Queue
    tw.queue.put(Message)
def Post11Message(gameDiscript):
    #Adds gameDiscript to Queue
    tw.queue.put(gameDiscript)


main()