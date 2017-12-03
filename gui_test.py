from tkinter import *
master = Tk()

canvas_width = 1280
canvas_height = 720
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
#w.create_line(0, y, canvas_width, y, fill="#476042")
w.create_rectangle(0, 0, canvas_width, y, fill='#000000')

mainloop()
