import tkinter
from pytube import YouTube
root = tkinter.Tk()
# Canvas is used to created a window
canvas1 = tkinter.Canvas(root, width=400, height=300)
Entry = tkinter.Entry(root)
canvas1.create_window(200, 140, window=Entry)

title_label = tkinter.Label(text="Calculate The Square Root")
canvas1.create_window(200, 50, window=title_label)


def getSquareRoot():
    x1 = Entry.get()
    label1 = tkinter.Label(root, text="Download Completed")
    yt = YouTube(x1)
    yt = yt.streams.first()
    yt.download('/home/codewar/Videos/Down_Vidoes')
    canvas1.create_window(200, 230, window=label1)


button1 = tkinter.Button(text="Get the Square Root", command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)
canvas1.pack()
root.mainloop()
