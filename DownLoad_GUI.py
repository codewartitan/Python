import tkinter

root = tkinter.Tk()
# Canvas is used to created a window
canvas1 = tkinter.Canvas(root, width=400, height=300)
Entry = tkinter.Entry(root)
canvas1.create_window(200, 140, window=Entry)


def getSquareRoot():
    x1 = Entry.get()
    label1 = tkinter.Label(root, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)


button1 = tkinter.Button(text="Get the Square Root", command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)
canvas1.pack()
root.mainloop()
