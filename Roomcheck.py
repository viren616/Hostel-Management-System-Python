from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
import threading
import time
from tkinter import messagebox
import Adminhome
import Home
import Foregtepw
class Roomcheck:
    def __init__(self):
        root = Tk()
        root.geometry('1369x769+0+0')
        root.overrideredirect(True)
        root.lift()
        root.attributes("-topmost", True)

        load = Image.open("E:/prog/qp/50c.jpg")
        load = load.resize((1373, 773), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=-5, y=-5)

        frame = Frame(img, width=1200, height=600,borderwidth=5)
        frame.place(x=80, y=80)
        load1 = Image.open("F:/image/2.jpg")
        load1 = load1.resize((1196, 596), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(frame, image=render1)
        img1.image = render1
        img1.place(x=-5, y=-5)

        def close(event):
            root.destroy()

        border = Label(img1, bg='black', width=170, height=3)
        border.place(x=0, y=0)
        load2 = Image.open("E:/prog/qp/c.png")
        load2 = load2.resize((50, 45), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(border, image=render2, bg='black',cursor='hand2')
        img2.image = render2
        img2.place(x=1140, y=0)
        img2.bind("<Button>", close)

        def back(event):
            root.destroy()
            Home.Home()
        load3 = Image.open("E:/prog/qp/b1.png")
        load3 = load3.resize((50, 45), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(border, image=render3, bg='black',cursor='hand2')
        img3.image = render3
        img3.place(x=10, y=0)
        img3.bind("<Button>", back)


        canvas = Canvas(frame, bg='black', width=460)
        canvas.place(x=350, y=100)

        def loop1_10():
            i =0
            while i <= 350:
                time.sleep(.01)
                i = i + 5
                canvas.configure(height=i)
        threading.Thread(target=loop1_10).start()


        login = Label(canvas, text='Check Room Availability', font='Algerian  25  bold', bg='black', fg='firebrick')
        login.place(x=5, y=10)
        broom= Label(canvas, text='Boys Rooms', font='Algerian  15  ', bg='black', fg='firebrick')
        broom.place(x=20, y=140)
        groom = Label(canvas, text='Girls Rooms', font='Algerian  15  ', bg='black', fg='firebrick')
        groom.place(x=20, y=210)

        occupied= Label(canvas, text='Occupied ', font='Algerian  15', bg='black', fg='firebrick')
        occupied.place(x=160, y=100)
        available = Label(canvas, text='Available ', font='Algerian  15  ', bg='black', fg='firebrick')
        available.place(x=290, y=100)

        oeb = Entry(canvas, font='Arial  12  ', bg='black', fg='white', width=5)
        oeb.place(x=180, y=140)
        oeg= Entry(canvas, font='Arial  12  ', bg='black', fg='white', width=5)
        oeg.place(x=180, y=210)
        aeb = Entry(canvas, font='Arial  12  ', bg='black', fg='white', width=5)
        aeb.place(x=300, y=140)
        aeg = Entry(canvas, font='Arial  12  ', bg='black', fg='white', width=5)
        aeg.place(x=300, y=210)


        try:
            global id
            mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur1 = mydb.cursor()
            cur1.execute("select * from room")
            rec1 = cur1.fetchall()
            for xx in rec1:
                oeb.insert(0, xx[0])
                oeb.configure(state='disabled', font='Arial  12  ', bg='black', fg='white', width=5)
                oeg.insert(0, xx[1])
                oeg.configure(state='disabled')

                aeb.insert(0,xx[2])
                aeb.configure(state='disabled', font='Arial  12  ', bg='black', fg='white', width=5)
                aeg.insert(0,xx[3])
                aeg.configure(state='disabled')

        except:
            print('d')



        #b = Button(canvas, text="Check Availability",command=proceeed, width=10,cursor='hand2',font='Algerian ', bg='black', fg='firebrick')
        #b.place(x=240, y=280)
        #b.bind("<Button>", proceeed)


        root.mainloop()


#Roomcheck()