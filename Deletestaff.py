from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
import Student
import Staff
from tkinter import filedialog
from tkinter import messagebox
class Deletestaff:
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
        frame = Frame(img, width=1200, height=600, borderwidth=5)
        # frame.place(x=80, y=80)
        load1 = Image.open("F:/image/2.jpg")
        load1 = load1.resize((1196, 596), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(frame, image=render1)
        img1.image = render1
        img1.place(x=-5, y=-5)

        def dialogfile(self):
            path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
            load4 = Image.open(path)
            load4 = load4.resize((120, 120), Image.ANTIALIAS)
            render4 = ImageTk.PhotoImage(load4)
            img4 = Label(frame, image=render4, width=120, height=120)
            img4.image = render4
            img4.place(x=510, y=40)

        id = Label(img1, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id.place(x=10, y=10)
        ide = Entry(img1, width=5, font='Arial  12', bg='white', fg='black')
        ide.place(x=80, y=10)
        name = Label(img1, text='Enter Name', font='Arial  12', bg='black', fg='white', width=13)
        name.place(x=20, y=70)
        namee = Label(img1, font='Arial  12', bg='white', fg='black')
        namee.place(x=180, y=70)
        fname = Label(img1, text='Enter Father Name', font='Arial  12', bg='black', fg='white', width=16)
        fname.place(x=20, y=130)
        fnamee = Label(img1, font='Arial  12', bg='white', fg='black')
        fnamee.place(x=180, y=130)
        dob = Label(img1, text='Date Of Birth', font='Arial  12', bg='black', fg='white', width=16)
        dob.place(x=20, y=190)
        dobe = Label(img1, width=27, bg="darkblue", fg="white")
        dobe.place(x=180, y=190)
        qualif = Label(img1, text='Qualification', font='Arial  12', bg='black', fg='white', width=16)
        qualif.place(x=20, y=250)
        qualife = Label(img1, font='Arial  12', bg='white', fg='black')
        qualife.place(x=180, y=250)
        gender = Label(img1, text='Gender', font='Arial  12', bg='black', fg='white', width=16)
        gender.place(x=20, y=310)
        gendere = Label(img1, text='Gender', font='Arial  12', bg='black', fg='white', width=16)
        gendere.place(x=180, y=310)

        email = Label(img1, text='Email', font='Arial  12', bg='black', fg='white', width=16)
        email.place(x=20, y=380)
        # email.bind("<Button>",check)
        emaile = Label(img1, font='Arial  12', bg='white', fg='black')
        emaile.place(x=180, y=380)
        number = Label(img1, text='Contact Number', font='Arial  12', bg='black', fg='white', width=16)
        number.place(x=20, y=440)
        numbere = Label(img1, font='Arial  12', bg='white', fg='black')
        numbere.place(x=180, y=440)

        adrs = Label(img1, text='Address', font='Arial  12', bg='black', fg='white', width=16)
        adrs.place(x=800, y=70)

        adrse = Label(img1, font='Arial  12', bg='white', fg='black', width=40)
        adrse.place(x=800, y=100)
        streetadrs = Label(img1, text='Street Address', font='Arial  8', bg='black', fg='white', width=16)
        streetadrs.place(x=800, y=122)

        adrse2 = Label(img1, font='Arial  12', bg='white', fg='black', width=35)
        adrse2.place(x=800, y=150)
        streetadrs2 = Label(img1, text='Street Address 2', font='Arial  8', bg='black', fg='white', width=16)
        streetadrs2.place(x=800, y=172)

        city = Label(img1, font='Arial  12', bg='white', fg='black', width=18)
        city.place(x=800, y=210)
        cityl = Label(img1, text='City', font='Arial  8', bg='black', fg='white', width=16)
        cityl.place(x=800, y=232)

        state = Label(img1, font='Arial  12', bg='white', fg='black', width=18)
        state.place(x=1000, y=210)
        statel = Label(img1, text='State', font='Arial  8', bg='black', fg='white', width=16)
        statel.place(x=1000, y=232)

        pin = Label(img1, font='Arial  12', bg='white', fg='black', width=18)
        pin.place(x=800, y=270)
        pinl = Label(img1, text='Postal / Zip Code', font='Arial  8', bg='black', fg='white', width=16)
        pinl.place(x=800, y=292)

        def proceeed():
            global id
            id = usere.get()

            if (usere.get() == '' or fe.get()==''):
                messagebox.showinfo('message', 'please fill the details')
            else:
                f = 0
                global ss
                ss = usere.get()
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur1 = mydb.cursor()
                cur1.execute("select * from staffreg where name ='" + ss + "'")
                rec1 = cur1.fetchall()
                for xx in rec1:
                    if (usere.get() == xx[1]):
                        if (fe.get() == xx[2]):
                            f = 1
                            break
                if (f == 1):
                    frame1.destroy()
                    frame.place(x=80, y=80)
                    frame1.destroy()
                    frame.place(x=80, y=80)
                    ide.insert(0, xx[0])
                    ide.configure(state='disabled')
                    namee.configure(text=xx[1], font='Algerian  ', bg='black', fg='firebrick')
                    fnamee.configure(text=xx[2], font='Algerian  ', bg='black', fg='firebrick')
                    dobe.configure(text=xx[3], font='Algerian  ', bg='black', fg='firebrick', width=16)
                    qualife.configure(text=xx[4], font='Algerian  ', bg='black', fg='firebrick')
                    gendere.configure(text=xx[5], font='Algerian  ', bg='black', fg='firebrick')
                    emaile.configure(text=xx[6], font='Algerian  ', bg='black', fg='firebrick')
                    numbere.configure(text=xx[7], font='Algerian  ', bg='black', fg='firebrick')

                    adrse.configure(text=xx[8], font='Algerian  ', bg='black', fg='firebrick', width=16)
                    adrse2.configure(text=xx[9], font='Algerian  ', bg='black', fg='firebrick')
                    city.configure(text=xx[10], font='Algerian  ', bg='black', fg='firebrick')
                    state.configure(text=xx[11], font='Algerian  ', bg='black', fg='firebrick')
                    pin.configure(text=xx[12], font='Algerian  ', bg='black', fg='firebrick')

                else:
                    messagebox.showinfo('message', 'Invalid user')

        proceed = Button(frame1, text='Proceed', width=15, command=lambda:[proceeed()], font='Algerian  ', bg='black', fg='firebrick')
        proceed.place(x=1000, y=500)

        def connect(event):
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur = mydb.cursor()
            cur1 = mydb.cursor()
            cur2 = mydb.cursor()
            sql = " insert into exstaff select * from staffreg where id ='"+ide.get()+"'"
            sql1 = " delete from staffreg where id ='"+ide.get()+"'"
            sql2 = " delete from staffpass where id ='" + ide.get() + "'"
            try:
                cur.execute(sql)
                cur1.execute(sql1)
                cur2.execute(sql2)
                mydb.commit()
                messagebox.showinfo('message', 'inserted')
            except:
                print('f')
                mydb.rollback()

            mydb.close()
            root.destroy()
            Staff.Staff()
        submit = Button(frame, text="Submit", width=15,  font='Algerian  ', bg='black', fg='firebrick')
        submit.place(x=500, y=500)
        submit.bind('<Button>', connect)

        root.mainloop()
#Deletestaff()