from tkinter import *
from tkinter.ttk import *


root = Tk()
style =Style()
style.configure('w.Label', background='white')

l1 = Label(text="Test", style="w.Label")
l2 = Label(text="Test", style="BW.TLabel")
l1.pack()
mainloop()
