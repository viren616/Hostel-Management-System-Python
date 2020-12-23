from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import Adminlogin
import Createpw
class Frogetpw:
    def __init__(self):
        root = Tk()
        root.geometry('1200x600+80+80')
        root.overrideredirect(True)
        root.lift()
        root.attributes("-topmost",False)

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
            Adminlogin.Adminlogin()
        load3 = Image.open("E:/prog/qp/b1.png")
        load3 = load3.resize((50, 45), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(border, image=render3, bg='black',cursor='hand2')
        img3.image = render3
        img3.place(x=10, y=0)
        img3.bind("<Button>", back)

        canvas1 = Canvas(img, bg='gray', height=400, width=500)
        canvas1.place(x=350, y=100)

        fg=Label(canvas1,text='Forget Password', font='Arial  22 ', bg='gray', fg='black')
        fg.place(x=120,y=30)
        name = Label(canvas1, text='Enter Name', font='Arial  15 ', bg='gray', fg='black')
        name.place(x=40, y=130)
        fname = Label(canvas1, text='Enter Father Name', font='Arial  15 ', bg='gray', fg='black')
        fname.place(x=40, y=190)
        dob = Label(canvas1, text='Enter DOB', font='Arial  15 ', bg='gray', fg='black')
        dob.place(x=40, y=260)

        namee=Entry(canvas1,width=25,font='Arial  12  ', bg='white', fg='black')
        namee.place(x=250,y=130)
        fnamee=Entry(canvas1,width=25,font='Arial  12  ', bg='white', fg='black')
        fnamee.place(x=250,y=190)
        dobe=Entry(canvas1,width=25,font='Arial  12  ', bg='white', fg='black')
        dobe.place(x=250,y=260)
        #canvas 2/////////////////////////////////////////////////////////

        canvas2 = Canvas(img, bg='gray', height=400, width=500)
        #canvas2.place(x=350, y=100)
        id = Label(canvas2, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id.place(x=10, y=90)
        ide = Entry(canvas2, width=5, font='Arial  12', bg='white', fg='black')
        ide.place(x=80, y=90)

        fg = Label(canvas2, text='Create Password', font='Arial  22 ', bg='gray', fg='black')
        fg.place(x=120, y=30)
        password = Label(canvas2, text='Enter Password', font='Arial  15 ', bg='gray', fg='black')
        password.place(x=40, y=150)
        password1 = Label(canvas2, text='Conform Password', font='Arial  15 ', bg='gray', fg='black')
        password1.place(x=40, y=210)

        passe = Entry(canvas2, width=25, font='Arial  12  ', bg='white', fg='black')
        passe.place(x=250, y=150)
        conforme = Entry(canvas2, width=25, font='Arial  12  ', bg='white', fg='black')
        conforme.place(x=250, y=210)
        global x

        def pp(event):
            if (namee.get() == '' or fnamee.get()=='' or dobe.get()=='' ):
                messagebox.showinfo('message', 'please fill the details')
            else:
                f = 0
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                cur.execute("select * from studreg")
                rec = cur.fetchall()
                for x in rec:
                    if (namee.get() == x[1]):
                        if (fnamee.get() == x[2]):
                            if (dobe.get() == x[3]):
                                f = 1
                                break
                if (f == 1):
                    canvas1.destroy()
                    ide.insert(0, x[0])
                    ide.configure(state='disabled')
                    canvas2.place(x=350,y=100)
                else:
                    messagebox.showinfo('message', 'Invalid user')

        def check(event):
            root.destroy()
            #Createpw.Createpw()

        close=Button(canvas1,text='Submit',width=30,fg='white',bg='black',activebackground='white',activeforeground='black',cursor='hand2')
        close.place(x=250,y=350)
        close.bind('<Button>',pp)


        def connect(event):
            global idc

            if (passe.get() != conforme.get()):
                messagebox.showinfo('message', 'Password Not Match')
            else:
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur1 = mydb.cursor()
                sql1 = "update password set pass=%s where id=%s"
                a = ide.get()
                b = passe.get()
                value1 = (b,a)
            try:
                cur1.execute(sql1, value1)
                mydb.commit()
                messagebox.showinfo('message', 'update')
            except:
                mydb.rollback()
            mydb.close()
            root.destroy()
            Adminlogin.Adminlogin()
        close = Button(canvas2, text='Update', width=30, fg='white', bg='black', activebackground='white',
                       activeforeground='black', cursor='hand2')
        close.place(x=250, y=350)
        close.bind('<Button>', connect)

        root.mainloop()
#Frogetpw()