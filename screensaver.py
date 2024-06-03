#-*-coding:utf-8-*-

import os
import time
import tkinter
from tkinter import *

WORK_PATH=os.path.abspath(os.getcwd())

root=Tk()#это и есть то самое главное окошко!
root.overrideredirect(1)#а теперь мы виджет))аргументы True/False
root.geometry("100x100+0+0")#задаем размер 100 на 100 пикселей и координаты размещения на экране.
bg_image=PhotoImage(os.path.join(WORK_PATH,'bg.gif'))#вот нам и пригодился WORK_PATH! os.path.join()-соединяет пути. PhotoImage-загружаем изображение.
bg=Label(root,image=bg_image)#создаем метку(текст как бэ) но вместо текста ставим изображение(хе-хе,хитрюги =)).
bg.pack()#заливаем фон.(вообще,это позиционирование,но в данном случае мы именно заливаем фон.

def clock(event):
    time_from_out=time.strftime("%H:%M:%S")
    clock_value=Label(root,bg='black',fg='green',text=time_from_out,font=('Comic Sans MS',8))#создаем текстовую метку,она будет показывать время. bg-фон метки,fg-цвет текста,font-параметры шрифта.
    while event:
        clock_value.place(x='20',y='20')#размещаем наше время
        root.update()#обновляем окошко





