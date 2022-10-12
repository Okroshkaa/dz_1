import tkinter
import math
tk = tkinter.Tk() # Создает окно
tk.title('заголовок') # Заголовок


button = tkinter.Button(tk) # Создание кнопки
button['text'] = 'Закрыть'
button['command'] = tk.quit
button.pack()

canvas = tkinter.Canvas(tk) #Создали рабочую область в окне tk
canvas['height'] = 360 # Высота
canvas['width'] = 480 # Ширина
canvas['background'] = '#eeeeff'
canvas['borderwidth'] = 2
canvas.pack()

canvas.create_text(20,10, text='арбуз')
canvas.create_text(460,350, text='дыня')

points = [] # создаем список
ay = 150
y0 = 150
x0 = 50
x1 = 470
dx = 10

for n in range(x0,x1,dx):  # для n в диапозоне от x0 до x1 с шагом dx
    y = y0 - ay * math.cos(n*dx)
    pp = (n,y)
    points.append(pp)   # закрываем список
canvas.create_line(points, fill='blue', smooth=1)

y_axe =[]
yy = (x0,0)
y_axe.append(yy)
yy=(x0,y0+ay)
y_axe.append(yy)
canvas.create_line(y_axe, fill = 'black', width = 2)



tk.mainloop()

