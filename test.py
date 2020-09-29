# from tkinter import *
#
# # Top level window
# window = Tk()
#
# window.title("Studyfied.com")
# window.geometry('350x200')
#
# # Option menu variable
# optionVar = StringVar()
# optionVar.set("Red")
#
# # Create a option menu
# option = OptionMenu(window, optionVar, "Red", "Blue", "White", "Black")
# option.pack()
#
# # Create button with command
# def show():
#     print("Selected value :", optionVar.get())
#
# btnShow = Button(window, text="Show", command=show)
# btnShow.pack()
#
# window.mainloop()

# from change_template import Templates
#
# t = Templates()
#
# # print(t.template['CER']['title'])
# for item in t.template['CER']['ini']:
#     print

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://jefferson.service-now.com/navpage.do')
print(driver.title)
driver.minimize_window()
time.sleep(5)
print(driver.title)
