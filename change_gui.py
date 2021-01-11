from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from changes import CreateChange
from change_template import Templates as tp
import re
import os
import pickle

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()
        self.session = None

    def init_window(self):

        self.master.title('Automated Change Tickets')
        self.pack(fill=BOTH, expand=1)

        if os.path.exists('data/settings.pickle'):
            with open('data/settings.pickle', 'rb') as handle:
                settings = pickle.load(handle)
                settings_exist = True
        else:
            if not os.path.exists('./data'):
                os.mkdir('./data')
            settings_exist = False

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save', command=self.client_exit)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Nothing here', command=None)
        menu.add_cascade(label='Edit', menu=edit)

        view = Menu(menu)
        view.add_command(label='View Recent Report', command=None)
        menu.add_cascade(label='View', menu=view)

        msg = Message(
                        self,
                        text="Welcome to Matthew Moore's Automated Change Tickets, made painstakingly by me, Matthew Moore.",
                        bg='#4c9dd5',
                        bd=20,
                        fg='black',
                        aspect=530,
                        width=500,
                        justify='center',
                        font=('TkDefaultFont', 9, 'bold'),
                    )
        msg.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        campus_key_label = Label(self, text='Campus Key')
        campus_key_label.place(relx=-0.150, rely=0.11, relwidth=0.5, relheight=0.07)

        self.campus_key = StringVar()
        self.campus_key_entry = Entry(self, textvariable=self.campus_key)
        self.campus_key_entry.place(relx=0.03, rely=0.17, relwidth=0.4, relheight=0.07)

        password_label = Label(self, text='Password')
        password_label.place(relx=-0.165, rely=0.25, relwidth=0.5, relheight=0.07)

        self.password_entry = Entry(self, show='*')
        self.password_entry.place(relx=0.03, rely=0.32, relwidth=0.4, relheight=0.07)
        self.password = self.password_entry

        ini_label = Label(self, text='Master File')
        ini_label.place(relx=-0.11, rely=0.4, relwidth=0.4, relheight=0.07)

        self.options = StringVar()
        self.ini_entry = OptionMenu(self, self.options, *tp.ebi_files)
        self.ini_entry.place(relx=0.03, rely=0.47, relwidth=0.4, relheight=0.07)
        self.ini = self.options

        self.save_settings = IntVar()
        save_setting_box = Checkbutton(self, text='Save Settings',
                                      selectcolor='#4c9dd5', variable=self.save_settings,
                                      command='')
        save_setting_box.place(relx=-0.03, rely=0.58, relwidth=0.4, relheight=0.07)

        submit_btn = Button(self, text='Create Change', command=self.submit_clicked)
        submit_btn.place(relx=0.03, rely=0.7)

        clear_btn = Button(self, text='Clear Data', command=self.clear_all_entries)
        clear_btn.place(relx=0.28, rely=0.7)

        # https://stackoverflow.com/questions/37234071/changing-the-background-color-of-a-radio-button-with-tkinter-in-python-3
        style = ttk.Style()                     # Creating style element
        style.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
                        background='#4c9dd5',   # Setting background to our specified color above
                        foreground='black')     # You can define colors like this also

        self.app = StringVar()
        app_label = Label(self, text="Application")
        app_label.place(relx=-0.150, rely=0.85, relwidth=0.5, relheight=0.07)

        ebi_radial_btn = ttk.Radiobutton(self,text='EBI',value='EBI',variable=self.app,command=self.app_type,style='Wild.TRadiobutton')
        ebi_radial_btn.place(relx=0.03,rely=0.9)

        hp_radial_btn = ttk.Radiobutton(self,text='Healthy Planet',value="Healthy Planet",variable=self.app, command=self.app_type,style='Wild.TRadiobutton')
        hp_radial_btn.place(relx=0.15,rely=0.9)

        load = Image.open('img/Globe-Internet-icon.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(relx=0.5, rely=0.13)

        if settings_exist:
            self.campus_key.set(settings['campus_key'])
            self.app.set(settings['app'])
            self.app_type()
            self.password_entry.focus()
        else:
            self.campus_key_entry.focus()

    def client_exit(self):
        exit() # built-in python function

    def update_lst(self, dropdown, files):
        dropdown['menu'].delete(0,'end') # remove the entries
        for ini in files: #update the optionMenu variable with new list of values
            dropdown['menu'].add_command(label=ini,command=lambda name=ini: self.options.set(name))
        return dropdown

    def app_type(self):
        if self.app.get() == 'EBI':
            self.update_lst(self.ini_entry, tp.ebi_files)
        else:
            self.update_lst(self.ini_entry, tp.master_files)
        print(self.app.get())
        print(self.options)

    def validate_entry(self):
        if not all([self.campus_key.get(), self.password.get(), self.ini.get()]):
            return False
        return True

    def clear_all_entries(self):
        self.campus_key_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.options.set('')
        self.campus_key_entry.focus()

    def clear_login_entry(self):
        self.campus_key_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.campus_key_entry.focus()

    def session_is_alive(self, driver):
        try:
            driver.title
            return True
        except:
            return False

    def submit_clicked(self):
        print(self.app.get())
        if self.validate_entry():
            login_settings ={
                'userid':self.campus_key.get(),
                'password':self.password.get(),
                'ini':self.ini.get()[0:3]
            }
            if self.save_settings.get()==1:
                with open('data/settings.pickle', 'wb') as handle:
                    pickle_settings = {'campus_key':self.campus_key_entry.get(),'app':self.app.get()}
                    pickle.dump(pickle_settings, handle)

            try: # check to see if there's an existing minimized window and update login settings
                self.session.check_title()
                self.session.update_login_settings(login_settings)
            except: # no existing title, so create new browser
                self.session = CreateChange(login_settings)
                self.session.start_browser()

            try:
                self.session.login()
                self.session.create_change()
            except Exception as e:
                self.session.driver.minimize_window()
                messagebox.showerror('Hold Up', 'Wrong username/password')
                self.clear_login_entry()
                print(e)

        else:
            messagebox.showerror('This is so wrong', 'One or more entries are missing')

root = Tk() # define root window
root.geometry('600x400')
app = Window(root) # reference window class with root

sp = os.getcwd() # get the path of the current directory
imgicon = PhotoImage(file=os.path.join(sp,'img/Globe-Internet-icon.png'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.mainloop() # generates window
