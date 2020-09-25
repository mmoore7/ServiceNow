from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import os
import pickle

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Healthy Planet Automated Change Tickets")
        self.pack(fill=BOTH, expand=1)

        if os.path.exists('data/settings.pickle'):
            with open('data/settings.pickle', 'rb') as handle:
                settings = pickle.load(handle)
                settings_exist = True
        else:
            if not os.path.exists('./data'):
                os.mkdir('./data')
            settings_exist = False

        self.change_types = ['CER - Rules', 'VCG - Grouper']
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Save", command=self.client_exit)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label='Nothing here', command=None)
        menu.add_cascade(label='Edit', menu=edit)

        view = Menu(menu)
        view.add_command(label='View Recent Report', command=None)
        menu.add_cascade(label='View', menu=view)

        msg = Message(
                        self,
                        text="Welcome to Matthew Moore's Automated Change Tickets, made painstakingly by me, Matthew Moore.",
                        bg="#696969",
                        aspect=530,
                        width=500,
                        justify='center'
                    )
        msg.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        campus_key_label = Label(self, text="Campus Key")
        campus_key_label.place(relx=-0.150, rely=0.11, relwidth=0.5, relheight=0.07)

        self.login = StringVar()
        if settings_exist:
            self.login.set(setttings['userid'])
        campus_key_entry = Entry(self, textvariable=self.login)
        campus_key_entry.focus()
        campus_key_entry.place(relx=0.03, rely=0.17, relwidth=0.4, relheight=0.07)

        password_label = Label(self, text="Password")
        password_label.place(relx=-0.165, rely=0.25, relwidth=0.5, relheight=0.07)

        password_entry = Entry(self, show='*')
        password_entry.place(relx=0.03, rely=0.32, relwidth=0.4, relheight=0.07)

        ini_label = Label(self, text='Master File')
        ini_label.place(relx=-0.11, rely=0.4, relwidth=0.4, relheight=0.07)

        ini_entry = OptionMenu(self, StringVar(),'CER - Rules', 'VCG - Grouper')
        ini_entry.place(relx=0.03, rely=0.47, relwidth=0.4, relheight=0.07)

    def client_exit(self):
        exit() # built-in python function

root = Tk() # define root window
root.geometry("600x400")
app = Window(root) # reference window class with root

sp = os.getcwd() # get the path of the current directory
# imgicon = PhotoImage(file=os.path.join(sp,'img/cash-credit.png'))
# root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.mainloop() # generates window
