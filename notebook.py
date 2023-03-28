from tkinter import *
from tkinter import ttk

#copy and pasted code to make an example notebook
#just here for when i want to make my own notebook widgets

root = Tk()
root.title("notebook")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(pady=15)

frame1 = Frame(notebook,bg="blue")
frame2 = Frame(notebook,bg="red")

frame1.pack(fill="both",expand=1)
frame2.pack(fill="both",expand=1)

notebook.add(frame1,text="blue tab")
notebook.add(frame2,text="blue tab")

root.mainloop()