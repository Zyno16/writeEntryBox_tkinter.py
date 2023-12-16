from tkinter import *
form = Tk()

form.geometry("700x500")

Label(form,text="Entry your name", bg = "navy",font = "consolas 30 underline" ).pack()
svname = StringVar()
txtname =Entry(form ,bg ="yellow" ,fg = "blue" ,font ="consolas 30 bold",textvariable = svname)
svname.set("empty")

txtname.pack()
form.mainloop()
