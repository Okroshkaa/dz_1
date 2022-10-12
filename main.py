import tkinter
import math


select = 0

def selection(choice):
    global select
    select = variable.get()
tk = tkinter.Tk()
tk.title('дз1')
button = tkinter.Button(
    text = "Закрыть",
    width = 8,
    height = 2,
    bg = '#00FFFF',
    fg = 'black',
    command = tk.quit,
    )

button.pack()
button.place(x=387,y=0)






optionlist = ['y=Ax+B','y=Ax+B/x','y=Ax^2','y=Acos(B*x)']

variable = tkinter.StringVar(tk)
variable.set(optionlist[0])



op = tkinter.OptionMenu(tk, variable, *optionlist, command = selection)
op.config(width = 9, height = 2)


op.pack(anchor = 'nw')








canvas = tkinter.Canvas(tk)
canvas['height']=360
canvas['width']=480
canvas['background']='#ffffff'
canvas['borderwidth']='2'
canvas.pack()

def osi():
    canvas.create_text(10,10,text='Y')
    canvas.create_text(470,350,text='X')
    canvas.create_text(10,350,text='0')
    points = []
    y_axe=[]
    yy = (22,10)
    y_axe.append(yy)
    yy =(22,335)
    y_axe.append(yy)
    canvas.create_line(y_axe,fill='black')
    y1_axe=[]
    yy = (22,335)
    y1_axe.append(yy)
    yy =(470,335)
    y1_axe.append(yy)
    canvas.create_line(y1_axe,fill='black')
    y2_axe=[]
    yy = (460,330)
    y2_axe.append(yy)
    yy =(470,335)
    y2_axe.append(yy)
    canvas.create_line(y2_axe,fill='black')
    y3_axe=[]
    yy = (460,340)
    y3_axe.append(yy)
    yy =(470,335)
    y3_axe.append(yy)
    canvas.create_line(y3_axe,fill='black')
    y4_axe=[]
    yy = (22,10)
    y4_axe.append(yy)
    yy =(17,20)
    y4_axe.append(yy)
    canvas.create_line(y4_axe,fill='black')
    y5_axe=[]
    yy = (22,10)
    y5_axe.append(yy)
    yy =(27,20)
    y5_axe.append(yy)
    canvas.create_line(y5_axe,fill='black')

def clear():
    canvas.delete("all")
    osi()

def one():
    y6_axe = []
    yy = (22, 335)
    y6_axe.append(yy)
    yy = (470, 20)
    y6_axe.append(yy)
    canvas.create_line(y6_axe, fill='black')

def two():
    points = []
    for i in range(35, 4000, 5):
        x = i / 10
        y = -1000 / x
        pp = (x + 40, y + 320)
        points.append(pp)
    canvas.create_line(points, fill='red', smooth=1)

def three():
    points = []
    for i in range(0, 780, 1):
        x = i / 10
        y = -0.05 * x * x
        pp1 = (x + 23, y + 334)
        points.append(pp1)
    canvas.create_line(points, fill='blue', smooth=1)

def four():
    points = []
    for i in range(0, 400, 12):
        x = i
        y = 100 * math.cos(i)
        pp1 = (x + 23, y + 234)
        points.append(pp1)
    canvas.create_line(points, fill='green', smooth=1)


def confirm():

    if select == 'y=Ax+B':
        one()

    if select == 'y=Ax+B/x':
        two()

    if select == 'y=Ax^2':
        three()

    if select == 'y=Acos(B*x)':
        four()

accept = tkinter.Button(
        text="Применить",
        width=9,
        height=2,
        bg='#00FFFF',
        fg='black',
        command = confirm
)
accept.pack()
accept.place(x=124, y=0)

deletegraphic = tkinter.Button(
    text='Очистить',
    width = 8,
    height = 2,
    bg='#00FFFF',
    fg='black',
    command = clear
)
osi()
deletegraphic.pack()
deletegraphic.place(x=200,y=0)






tk.mainloop()
