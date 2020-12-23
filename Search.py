from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
import Student
import Staff
from tkinter import filedialog
from tkinter import messagebox
class Search:
    def __init__(self):
        root = Tk()
        root.geometry('1369x769+0+0')
        root.overrideredirect(True)
        root.lift()
        root.attributes("-topmost",True)

        load = Image.open("E:/prog/qp/50c.jpg")
        load = load.resize((1373, 773), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=-5, y=-5)
        label1=Label(img,font='Arial  25  bold', bg='black', fg='white',width=60)
        label1.place(x=80,y=35)
        def close(event):
            root.destroy()
        load2 = Image.open("E:/prog/qp/c.png")
        load2 = load2.resize((50, 40), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(label1, image=render2, bg='black',cursor='hand2')
        img2.image = render2
        img2.place(x=1150, y=0)
        img2.bind("<Button>", close)
        def back(event):
            root.destroy()
            Staff.Staff()
        load3 = Image.open("E:/prog/qp/b1.png")
        load3 = load3.resize((50, 40), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(label1, image=render3, bg='black',cursor='hand2')
        img3.image = render3
        img3.place(x=10, y=0)
        img3.bind("<Button>", back)

        frame1 = Frame(img, width=1200, height=600, borderwidth=5, bg='black', highlightcolor="red",highlightthickness=1)
        frame1.place(x=80, y=80)
        load31 = Image.open("F:/image/2.jpg")
        load31 = load31.resize((1192, 594), Image.ANTIALIAS)
        render31 = ImageTk.PhotoImage(load31)
        img31 = Label(frame1, image=render31, bg='black')
        img31.image = render31
        img31.place(x=-5, y=-5)

        canvas = Canvas(frame1, bg='black', width=400, height=350)
        canvas.place(x=350, y=100)

        login = Label(frame1, text='Delete Staff', font='Algerian  25  ', bg='black', fg='firebrick')
        login.place(x=430, y=0)
        l = Label(canvas, text='Please Enter Details', font='Algerian  25  ', bg='black', fg='firebrick')
        l.place(x=10, y=5)

        username = Label(canvas, text='Name', font='Algerian  15  ', bg='black', fg='firebrick')
        username.place(x=20, y=100)
        usere = Entry(canvas, font='Arial  12  ', bg='white', fg='black', width=15)
        usere.place(x=200, y=100)
        fe1 = Label(canvas, text='Father Name', font='Algerian  15  ', bg='black', fg='firebrick')
        fe1.place(x=20, y=180)
        fe = Entry(canvas, font='Arial  12  ', bg='white', fg='black', width=15)
        fe.place(x=200, y=180)

        # frame////////////////////////////////////////////
        #submit = Button(frame, text="Submit", width=15,  font='Algerian  ', bg='black', fg='firebrick')
        #submit.place(x=500, y=500)
        #submit.bind('<Button>', connect)

        root.mainloop()
Search()