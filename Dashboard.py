from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="").place(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).place(column=1, row=0)
root.mainloop()
