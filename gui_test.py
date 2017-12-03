import tkinter
master = tkinter.Tk()

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

canvas_width = 1280
canvas_height = 720
w = tkinter.Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()
thirdy = int(canvas_height / 3)
thirdx = int(canvas_width / 3)

w.create_rectangle(0, 0, thirdx, thirdy, fill="#D81E5B")
w.create_rectangle(thirdx, 0, thirdx*2, thirdy, fill="#3A3335")
w.create_rectangle(thirdx*2, 0, thirdx*3, thirdy, fill="#F0544F")

w.create_rectangle(0, thirdy, thirdx, thirdy, fill="#1C2321")
w.create_rectangle(thirdx, thirdy, thirdx*2, thirdy*2, fill="#7D98A1")
w.create_rectangle(thirdx*2, thirdy, thirdx*3, thirdy*2, fill="#5E6572")

w.create_rectangle(0, thirdy*2, thirdx, thirdy*3, fill="#A9B4C2")
w.create_rectangle(thirdx, thirdy*2, thirdx*2, thirdy*3, fill="#7D1D3F")
w.create_rectangle(thirdx*2, thirdy*2, thirdx*3, thirdy*3, fill="#84ACCE")

img = tkinter.PhotoImage(file = os.path.join(dir_path,'assets','apple.gif'))
w.create_image(0, 0, image = img, anchor='nw')

tkinter.mainloop()

