from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import threading
import time
import Student
import Staff
import Room
import Adminlogin
class Adminhome:
    def __init__(self):
        root = Tk()
        root.geometry('1369x769+0+0')
        root.overrideredirect(True)
        root.configure(bg='black')
        #root.lift()
        #root.attributes("-topmost", True)

        load1 = Image.open("F:/image/2.jpg")
        load1 = load1.resize((1110, 772), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(root, image=render1,bg='black')
        img1.image = render1
        img1.place(x=250, y=-5)

        def close(event):
            root.destroy()
        border = Label(img1, bg='black', width=160, height=3)
        border.place(x=0, y=0)
        load2 = Image.open("E:/prog/qp/c.png")
        load2 = load2.resize((50, 45), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(border, image=render2, bg='black',cursor='hand2')
        img2.image = render2
        img2.place(x=1050, y=0)
        img2.bind("<Button>", close)

        def back(event):
            root.destroy()
            Adminlogin.Adminlogin()
        load3 = Image.open("E:/prog/qp/b1.png")
        load3 = load3.resize((50, 45), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(border, image=render3, bg='black',cursor='hand2')
        img3.image = render3
        img3.place(x=10, y=0)
        img3.bind("<Button>", back)


        side = Frame(root, bg='black', width=250, height=770)
        side.place(x=-250, y=0)

        load4 = Image.open("E:/prog/qp/add.png")
        load4 = load4.resize((250, 250), Image.ANTIALIAS)
        render4 = ImageTk.PhotoImage(load4)
        img4 = Label(side, image=render4, bg='black')
        img4.image = render4
        img4.place(x=-5, y=-5)
        l = Label(side, text='Adminnistrator', font='Algerian  16  ', bg='black', fg='firebrick')
        l.place(x=38, y=220)

        def stud(event):
            root.destroy()
            Student.Student()
        l1 = Label(side, text='Student Module', font='Algerian  16  ', bg='black', fg='firebrick', cursor='hand2')
        l1.place(x=30, y=350)
        l1.bind('<Button>', stud)

        def stf(event):
            root.destroy()
            Staff.Staff()
        l2 = Label(side, text='Staff Module', font='Algerian  16  ', bg='black', fg='firebrick', cursor='hand2')
        l2.place(x=30, y=430)
        l2.bind('<Button>', stf)
        def room(event):
            root.destroy()
            Room.Room()
        l3 = Label(side, text='Rooms Module', font='Algerian  16  ', bg='black', fg='firebrick', cursor='hand2')
        l3.place(x=30, y=510)
        l3.bind('<Button>', room)

        l4 = Label(side, text='Admin', font='Algerian  16  ', bg='black', fg='firebrick', cursor='hand2')
        l4.place(x=30, y=590)

        def loop1_10():
            i = -250
            while i <= -10:
                time.sleep(.01)
                i = i + 5
                side.place(x=i, y=-5)
        threading.Thread(target=loop1_10).start()


        root.mainloop()
#Adminhome()