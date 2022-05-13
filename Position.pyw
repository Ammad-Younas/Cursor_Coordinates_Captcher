from tkinter import *
from tkinter import messagebox
import pyautogui
import keyboard
import pyperclip


window = Tk()
window.title('Cursor Position by - C-S')
window.iconbitmap('icon\logo.ico')
window.geometry("306x142+520+240")
window.resizable(False, False)


width_label = Label(window, text="Width", font=('Segoe Script', 20, "bold"), fg='red')
width_label.place(x=25, y=2)


height_label = Label(window, text="Height", font=('Segoe Script', 20, "bold"), fg='green')
height_label.place(x=185, y=2)



def info():
    messagebox.showinfo("Info!", "To copy the values....!\n\n1: Press x for width\n2: Press y for height\n3: Press c for both")


def count_down():
    pos = pyautogui.position()
    pos = (str(pos).replace("Point(x=", "").replace(" y=", "").replace(")", ""))
    x, y = pos.split(",")
    if len(x) == 3:
        x = "0" + str(x)
    elif len(x) == 2:
        x = "00" + str(x)
    elif len(x) == 1:
        x = "000" + str(x)
    if len(y) == 3:
        y = "0" + str(y)
    elif len(y) == 2:
        y = "00" + str(y)
    elif len(y) == 1:
        y = "000" + str(y)

    xvalue = Label(window, text=x, font=('Arial Bold', 40), bg='white', fg='green', bd=2, relief=GROOVE)
    xvalue.place(x=10, y=50)


    yvalue = Label(window, text=y, font=('Arial Bold', 40), bg='white', fg='red', bd=2, relief=GROOVE)
    yvalue.place(x=175, y=50)


    if keyboard.is_pressed('c'):
        pyperclip.copy(str(x)+" "+str(y))
        copy_label = Label(text="Copied!", font=('Segoe Script', 10, "bold"), bg='#f0f0f0', fg='blue')
        copy_label.place(x=122, y=120)
        window.after(1000, lambda: count_down())
    elif keyboard.is_pressed('x'):
        pyperclip.copy(str(x))
        copy_label = Label(text="Copied!", font=('Segoe Script', 10, "bold"), bg='#f0f0f0', fg='green')
        copy_label.place(x=122, y=120)
        window.after(1000, lambda: count_down())
    elif keyboard.is_pressed('y'):
        pyperclip.copy(str(y))
        copy_label = Label(text="Copied!", font=('Segoe Script', 10, "bold"), bg='#f0f0f0', fg='red')
        copy_label.place(x=122, y=120)
        window.after(1000, lambda: count_down())
    else:
        copy_label = Label(text="Copied!", font=('Segoe Script', 10, "bold"), bg='#f0f0f0', fg='#f0f0f0')
        copy_label.place(x=122, y=120)
        window.after(100, lambda: count_down())


count_down()


click_btn= PhotoImage(file='icon\info.png')
img_label= Label(image=click_btn)
button= Button(window, image=click_btn, command = info, border=0, background="#f0f0f0", activebackground="#f0f0f0", cursor="hand2")
button.place(x=140, y=80)


copy_label = Label(window, text="Copied!", font=('Segoe Script', 10, "bold"), fg='#f0f0f0', bg="#f0f0f0").place(x=122, y=120)


window.mainloop()