from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
import threading
import time
from tkinter import messagebox
import Adminhome
import Home
import forgetadminpw
import Foregtepw
class Adminlogin:
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


        canvas = Canvas(frame, bg='black', width=400)
        canvas.place(x=350, y=100)

        def loop1_10():
            i =0
            while i <= 350:
                time.sleep(.01)
                i = i + 5
                canvas.configure(height=i)
        threading.Thread(target=loop1_10).start()


        login = Label(canvas, text='Admin Login', font='Algerian  25  bold', bg='black', fg='firebrick')
        login.place(x=100, y=10)
        username = Label(canvas, text='User Name', font='Algerian  15  ', bg='black', fg='firebrick')
        username.place(x=40, y=100)
        passw = Label(canvas, text='Password', font='Algerian  15  ', bg='black', fg='firebrick')
        passw.place(x=40, y=170)

        usere = Entry(canvas, font='Arial  12  ', bg='white', fg='black', width=15)
        usere.place(x=180, y=100)
        passwe = Entry(canvas, font='Arial  12  ', bg='white', fg='black', width=15, show="*")
        passwe.place(x=180, y=170)

        def showpassword():
            if checkvar1.get() == 1:
                passwe["show"] = ''
            else:
                passwe['show'] = "*"

        checkvar1 = IntVar()
        chkbtn1 = Checkbutton(canvas, text="Show Password", activebackground="gray", variable=checkvar1, onvalue=1,offvalue=0, height=2, width=15, bg='black',fg='firebrick', command=showpassword,cursor='hand2')
        chkbtn1.bind(showpassword)
        chkbtn1.place(x=180, y=200)

        def pp(event):
            if (usere.get() == '' or passwe.get() == ''):
                messagebox.showinfo('message', 'please fill the details')
            else:
                f = 0
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                cur.execute("select *from admin")
                rec = cur.fetchall()
                for x in rec:
                    if (usere.get() == x[0]):
                        if (passwe.get() == x[1]):
                            f = 1
                            break
                if (f == 1):
                    root.destroy()
                    Adminhome.Adminhome()
                else:
                    messagebox.showinfo('message', 'Invalid user')

        b = Button(canvas, text="Login", width=10,cursor='hand2',font='Algerian ', bg='black', fg='firebrick')
        b.place(x=240, y=280)
        b.bind("<Button>", pp)

        def check(event):
            root.destroy()
            forgetadminpw.forgetadminpw()
        b1 = Button(canvas, text="Forget Password",  width=15,font='Algerian ', bg='black', fg='firebrick')
        b1.place(x=60, y=280)
        b1.bind("<Button>", check)

        root.mainloop()


#Adminlogin()