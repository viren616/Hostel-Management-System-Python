from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
from tkinter import messagebox
import threading
import time
import Student

#import Adminhome
class Removestud:
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
            #Student.Student()
        load2 = Image.open("E:/prog/qp/b1.png")
        load2 = load2.resize((50, 45), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(border, image=render2, bg='black',cursor='hand2')
        img2.image = render2
        img2.place(x=10, y=0)
        img2.bind("<Button>", back)

        # frame1111/////////////////////////////////

        frame1 = Frame(img, width=1200, height=600, borderwidth=5, bg='black', highlightcolor="red",highlightthickness=1)
        frame1.place(x=80, y=80)
        load31 = Image.open("F:/image/2.jpg")
        load31 = load31.resize((1192, 594), Image.ANTIALIAS)
        render31 = ImageTk.PhotoImage(load31)
        img31 = Label(frame1, image=render31, bg='black')
        img31.image = render31
        img31.place(x=-5, y=-5)

        canvas = Canvas(frame1, bg='black', width=400,height=350)
        canvas.place(x=350, y=100)


        login = Label(frame1, text='Remove Student', font='Algerian  25  ', bg='black', fg='firebrick')
        login.place(x=400, y=0)
        l = Label(canvas, text='Please Enter Details', font='Algerian  25  ', bg='black', fg='firebrick')
        l.place(x=10, y=5)

        username = Label(canvas, text='Student ID', font='Algerian  15  ', bg='black', fg='firebrick')
        username.place(x=40, y=100)
        passw = Label(canvas, text='Password', font='Algerian  15  ', bg='black', fg='firebrick')
        passw.place(x=40, y=170)

        usere = Entry(canvas, font='Arial  12  ', bg='white', fg='black', width=15)
        usere.place(x=180, y=100)
        passwe = Entry(canvas, font='Arial  12  ', bg='white', fg='black', width=15, show="*")
        passwe.place(x=180, y=170)

        frame = Frame(img, width=1200, height=600, borderwidth=5, bg='black', highlightcolor="red", highlightthickness=1)
        #frame.place(x=80, y=80)
        load3 = Image.open("F:/image/2.jpg")
        load3 = load3.resize((1192, 594), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(frame, image=render3, bg='black')
        img3.image = render3
        img3.place(x=-5, y=-5)
        id1 = Label(frame, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id1.place(x=10, y=10)
        ide1 = Entry(frame, width=5, font='Arial  12', bg='white', fg='black')
        ide1.place(x=80, y=10)

        def proceeed():
            global id
            id = usere.get()

            if (usere.get() == '' or passwe.get() == ''):
                messagebox.showinfo('message', 'please fill the details')
            else:
                f = 0
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                cur.execute("select*from password")
                rec = cur.fetchall()
                for x in rec:
                    if (usere.get() == x[0]):
                        if (passwe.get() == x[1]):
                            f = 1
                            break
                if (f == 1):
                    frame1.destroy()
                    frame.place(x=80, y=80)
                    ide1.insert(0,id)
                    ide1.configure(state='disabled')

                else:
                    messagebox.showinfo('message', 'Invalid user')

        proceed = Button(frame1, text='Proceed', width=15, command=proceeed, font='Algerian  ', bg='black',
                         fg='firebrick')
        proceed.place(x=1000, y=500)

        def showpassword():
            if checkvar1.get() == 1:
                passwe["show"] = ''
            else:
                passwe['show'] = "*"

        checkvar1 = IntVar()
        chkbtn1 = Checkbutton(canvas, text="Show Password", activebackground="gray", variable=checkvar1, onvalue=1,
                              offvalue=0, height=2, width=15, bg='gray', command=showpassword, cursor='hand2')
        chkbtn1.place(x=180, y=200)
        l = Label(frame, text='Please Enter Below Details', font='Algerian  25  ', bg='black', fg='firebrick',
                  cursor='hand2')
        l.place(x=340, y=-5)


        root.mainloop()
#Removestud()