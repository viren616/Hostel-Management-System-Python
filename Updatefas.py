from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
from tkinter import messagebox
import threading
import time
import Student

#import Adminhome
class Updatefas:
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
            Student.Student()
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


        login = Label(frame1, text='Add / Remove Student Facilities', font='Algerian  25  ', bg='black', fg='firebrick')
        login.place(x=300, y=0)
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
        l1 = Label(frame, text='Select Bed Type', font='Algerian  16  ', bg='black', fg='firebrick', cursor='hand2',
                   width=28)
        l1.place(x=0, y=50)
        radio1 = IntVar()
        R1 = Radiobutton(img3, text="Single Bed Room", variable=radio1, value=1, bg='black', fg='firebrick', height=2)
        R1.place(x=20, y=80)
        R2 = Radiobutton(img3, text="Double Sharing", variable=radio1, value=2, bg='black', fg='firebrick', height=2)
        R2.place(x=150, y=80)
        R3 = Radiobutton(img3, text="Triple Sharing", variable=radio1, value=3, bg='black', fg='firebrick', height=2)
        R3.place(x=272, y=80)

        l2 = Label(img3, text='Select Payment Mode', font='Algerian  16  ', bg='black', fg='firebrick', width=28)
        l2.place(x=0, y=180)
        radio2 = IntVar()
        R4 = Radiobutton(img3, text="Monthly", variable=radio2, value=1, bg='black', fg='firebrick', height=2, width=10)
        R4.place(x=20, y=210)
        R5 = Radiobutton(img3, text="Quaterly", variable=radio2, value=2, bg='black', fg='firebrick', height=2,
                         width=10)
        R5.place(x=150, y=210)
        R6 = Radiobutton(img3, text="Yearly", variable=radio2, value=3, bg='black', fg='firebrick', height=2, width=10)
        R6.place(x=272, y=210)

        l3 = Label(img3, text='Hostel Type', font='Algerian  16  ', bg='black', fg='firebrick', width=28)
        l3.place(x=0, y=320)
        radio3 = IntVar()
        R7 = Radiobutton(img3, text="Girls Hostel", variable=radio3, value=1, bg='black', fg='firebrick', height=2,
                         width=15)
        R7.place(x=50, y=350)
        R8 = Radiobutton(img3, text="Boys Hostel", variable=radio3, value=2, bg='black', fg='firebrick', height=2,
                         width=15)
        R8.place(x=237, y=350)

        l4 = Label(img3, text='Other Hostel Facilities', font='Algerian  16  ', bg='black', fg='firebrick', width=30)
        l4.place(x=800, y=50)
        checkvar1 = IntVar()
        checkvar2 = IntVar()
        checkvar3 = IntVar()
        checkvar4 = IntVar()
        checkvar5 = IntVar()
        chkbtn1 = Checkbutton(img3, text="GYM Facility", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=12,
                              bg='black', fg='firebrick')
        chkbtn2 = Checkbutton(img3, text="Sports", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=12,
                              bg='black', fg='firebrick')
        chkbtn3 = Checkbutton(img3, text="Mess", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=12,
                              bg='black', fg='firebrick')
        chkbtn4 = Checkbutton(img3, text="Transportation", variable=checkvar4, onvalue=1, offvalue=0, height=2,
                              width=12, bg='black', fg='firebrick')
        chkbtn5 = Checkbutton(img3, text="Internet", variable=checkvar5, onvalue=1, offvalue=0, height=2, width=12,
                              bg='black', fg='firebrick')
        chkbtn1.place(x=800, y=100)
        chkbtn2.place(x=800, y=150)
        chkbtn3.place(x=800, y=200)
        chkbtn4.place(x=800, y=250)
        chkbtn5.place(x=800, y=300)

        def connect(event):
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if (radio1.get() == 0):
                messagebox.showinfo('message', 'Please select bed type')
            elif (radio2.get() == 0):
                messagebox.showinfo('message', 'Please select payment mode')
            elif (radio3.get() == 0):
                messagebox.showinfo('message', 'Please select hostel type')

            else:
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                global qq
                qq = ide1.get()
                sql1 = "update fasility set bedtype=%s,payment=%s,roomtype=%s,gym=%s,sports=%s,mess=%s,transport=%s,internet=%s where id=%s "

                if (radio1.get() == 1):
                    a1 = "One"
                elif (radio1.get() == 2):
                    a1 = "Two"
                elif (radio1.get() == 3):
                    a1 = "Three"

                if (radio2.get() == 1):
                    b1 = "Monthly"
                elif (radio2.get() == 2):
                    b1 = "Quaterly"
                elif (radio2.get() == 3):
                    b1 = "Yearly"

                if (radio3.get() == 1):
                    c1 = "Girls"
                elif (radio3.get() == 2):
                    c1 = "Boys"

                if (checkvar1.get() == 1):
                    d1 = "Yes"
                else:
                    d1 = "No"
                if (checkvar2.get() == 1):
                    e1 = "Yes"
                else:
                    e1 = "no"

                if (checkvar3.get() == 1):
                    f1 = "Yes"
                else:
                    f1 = "no"

                if (checkvar4.get() == 1):
                    g1 = "Yes"
                else:
                    g1 = "no"

                if (checkvar5.get() == 1):
                    h1 = "Yes"
                else:
                    h1 = "no"
                a = ide1.get()
                value2 = (a1, b1, c1, d1, e1, f1, g1, h1, a)
                print(value2)
                try:
                    cur.execute(sql1, value2)
                    mydb.commit()
                    messagebox.showinfo('message', 'inserted')
                except:
                    mydb.rollback()
                mydb.close()
                root.destroy()
                Student.Student()


        submit = Button(frame, text='Update', width=15, font='Algerian  ', bg='black', fg='firebrick')
        submit.place(x=1000, y=500)
        submit.bind('<Button>', connect)

        root.mainloop()
#Updatefas()