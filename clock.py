from tkinter import *
from datetime import datetime

import pyglet
pyglet.font.add_file("DS-Digital.TTF")

# CORES
color1 = "#3d3d3d"  # preta
color2 = "#fafcff"  # branca
color3 = "#21c25c"  # verde
color4 = "#eb463b"  # vermelha
color5 = "#dedcdc"  # cinza
color6 = "#3080f0"  # azul


background = color1
color = color4

window = Tk()
window.title('Clockpy')
window.geometry("440x180")
window.resizable(width=FALSE, height=FALSE)
window.configure(bg=color1)


def clock():
    Time_now = datetime.now()
    Time = Time_now.strftime("%H:%M:%S")
    day_week = Time_now.strftime("%a")
    day_month = Time_now.day
    month = Time_now.strftime("%b")
    year = Time_now.strftime("%Y")
    
    l1.config(text=Time)
    l1.after(200, clock)
    l2.config(text=day_week + "  " + str(day_month) + "/" + str(month) + "/" + str(year))
    
    
l1 = Label(window, text="", font=("DS-Digital 95"), bg=background, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2 = Label(window, text="", font=("DS-Digital 20"), bg=background, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

clock()
window.mainloop()


