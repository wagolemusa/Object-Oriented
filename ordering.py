try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here


from tkinter import ttk
import random 
import datetime

root = Tk()
root.geometry("1350*650+0+0")
root.title("Online Ordering System")
root.configure(background='black')



root.mainloop()