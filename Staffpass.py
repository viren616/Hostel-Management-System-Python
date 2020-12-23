from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import Foregtepw
import Addstaff
from Foregtepw import *
class Staffpass:
    def __init__(self):
        root = Tk()
        root.geometry('1200x600+80+80')
        root.overrideredirect(True)
        root.lift()
        root.attributes("-topmost",True)
        load = Image.open("F:/image/2.jpg")
        load = load.resize((1205, 605), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=-5, y=-5)

        def close(event):
            root.destroy()


        border = Label(img, bg='black', width=170, height=3)
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
            Foregtepw.Frogetpw()
        load3 = Image.open("E:/prog/qp/b1.png")
        load3 = load3.resize((50, 45), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(border, image=render3, bg='black',cursor='hand2')
        img3.image = render3
        img3.place(x=10, y=0)
        img3.bind("<Button>", back)

        canvas = Canvas(img, bg='gray', height=400, width=500)
        canvas.place(x=350, y=100)
        id = Label(canvas, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id.place(x=10, y=90)
        ide = Entry(canvas, width=5, font='Arial  12', bg='white', fg='black')
        ide.place(x=80, y=90)

        fg=Label(canvas,text='Create Password', font='Arial  22 ', bg='gray', fg='black')
        fg.place(x=120,y=30)
        password = Label(canvas, text='Enter Password', font='Arial  15 ', bg='gray', fg='black')
        password.place(x=40, y=150)
        password1 = Label(canvas, text='Conform Password', font='Arial  15 ', bg='gray', fg='black')
        password1.place(x=40, y=210)

        passe=Entry(canvas,width=25,font='Arial  12  ', bg='white', fg='black')
        passe.place(x=250,y=150)
        conforme=Entry(canvas,width=25,font='Arial  12  ', bg='white', fg='black')
        conforme.place(x=250,y=210)
        try:
            mydb1 = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur1 = mydb1.cursor()
            try:
                cur1.execute("select id from staffreg order by id desc limit  1")
                str = cur1.fetchall()
                print(str)
                ide.insert(0, str)
                ide.configure(state='disabled')
            except:
                mydb1.rollback()
        except:
            print('n')

        def connect(event):
            global passec, conformec
            passec = passe.get()
            conformec = conforme.get()
            if (passe.get() != conforme.get()):
                messagebox.showinfo('message', 'Password Not Match')
            else:
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                sql = "insert into staffpass(id,pass) values (%s,%s)"
                a = ide.get()
                b = passe.get()
                value = (a, b)
            try:
                cur.execute(sql, value)
                mydb.commit()
                messagebox.showinfo('message', 'inserted')
            except:
                mydb.rollback()
            mydb.close()
            root.destroy()
            Addstaff.Addstaff()

        close=Button(canvas,text='Update',width=30,fg='white',bg='black',activebackground='white',activeforeground='black',cursor='hand2')
        close.place(x=250,y=350)
        close.bind('<Button>',connect)
        root.mainloop()
#Staffpass()