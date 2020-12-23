from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import threading
import time
import Updatestaff
import Adminhome
import Deletestaff
import Addstaff
class Staff:
    def __init__(self):
        root = Tk()
        root.geometry('1369x769+0+0')
        root.overrideredirect(True)
        root.configure(bg='black')
        #root.lift()
        #root.attributes("-topmost", True)

        load = Image.open("E:/prog/qp/50c.jpg")
        load = load.resize((1373, 773), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=-5, y=-5)


        def close(event):
            root.destroy()
        border = Label(img, bg='black', width=170, height=3)
        border.place(x=80, y=30)
        load1 = Image.open("E:/prog/qp/c.png")
        load1 = load1.resize((50, 45), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(border, image=render1, bg='black',cursor='hand2')
        img1.image = render1
        img1.place(x=1140, y=0)
        img1.bind("<Button>", close)

        def back(event):
            root.destroy()
            Adminhome.Adminhome()
        load2 = Image.open("E:/prog/qp/b1.png")
        load2 = load2.resize((50, 45), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(border, image=render2, bg='black',cursor='hand2')
        img2.image = render2
        img2.place(x=10, y=0)
        img2.bind("<Button>", back)

        frame = Frame(img, width=1200, height=600, borderwidth=5,bg='black',highlightcolor="red", highlightthickness=1)
        frame.place(x=80, y=80)
        load3= Image.open("F:/image/2.jpg")
        load3 = load3.resize((949, 594), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(frame, image=render3,bg='black')
        img3.image = render3
        img3.place(x=240, y=-5)

        side = Frame(frame, bg='black', height=594)
        side.place(x=0, y=-5)
        load4 = Image.open("E:/prog/qp/sr.png")
        load4= load4.resize((230, 90), Image.ANTIALIAS)
        render4 = ImageTk.PhotoImage(load4)
        img4= Label(side, image=render4,bg='black')
        img4.image = render4
        img4.place(x=-5, y=-5)


        def AddStud(event):
            root.destroy()
            Addstaff.Addstaff()

        l1=Label(side,text='Add Staff',font='Algerian  16  ',bg='black',fg='firebrick',cursor='hand2')
        l1.place(x=15,y=150)
        l1.bind('<Button>',AddStud)

        def delete(event):
            root.destroy()
            Deletestaff.Deletestaff()
        l2 = Label(side, text='Remove Staff', font='Algerian  16  ', bg='black', fg='firebrick',cursor='hand2')
        l2.place(x=15, y=210)
        l2.bind('<Button>',delete)

        def update(event):
            root.destroy()
            Updatestaff.Updatestaff()

        l3 = Label(side, text='Update Information', font='Algerian  16  ', bg='black', fg='firebrick',cursor='hand2')
        l3.place(x=15, y=270)
        l3.bind('<Button>',update)

        l4 = Label(side, text='Search Staff', font='Algerian  16  ', bg='black', fg='firebrick',cursor='hand2')
        l4.place(x=15, y=330)

        def loop1_10():
            i = 0
            while i <= 230:
                time.sleep(.01)
                i = i + 5
                side.configure(width=i)
        threading.Thread(target=loop1_10).start()


        #b.bind('<Button>',loop1_10)
        root.mainloop()
#Staff()