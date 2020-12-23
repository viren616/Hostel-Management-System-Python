from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
from tkinter import filedialog
import base64
import io
import PIL.Image
from tkinter import messagebox
import Createpw
import Home
class Selection:
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
            Home.Home()
        load2 = Image.open("E:/prog/qp/b1.png")
        load2 = load2.resize((50, 45), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(border, image=render2, bg='black',cursor='hand2')
        img2.image = render2
        img2.place(x=10, y=0)
        img2.bind("<Button>", back)

        # new form.////////////
        frame2 = Frame(img, width=1200, height=600, borderwidth=5)
        load12 = Image.open("F:/image/2.jpg")
        load12 = load12.resize((1196, 596), Image.ANTIALIAS)
        render12 = ImageTk.PhotoImage(load12)
        img12 = Label(frame2, image=render12)
        img12.image = render12
        img12.place(x=-5, y=-5)
        id = Label(frame2, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id.place(x=10, y=10)
        ide = Entry(frame2, width=5, font='Arial  12', bg='white', fg='black')
        ide.place(x=80, y=10)

        name = Label(frame2, text='Enter Name', font='Arial  12', bg='black', fg='white', width=13)
        name.place(x=20, y=70)
        namee = Entry(frame2, font='Arial  12', bg='white', fg='black')
        namee.place(x=180, y=70)
        fname = Label(frame2, text='Enter Father Name', font='Arial  12', bg='black', fg='white', width=16)
        fname.place(x=20, y=130)
        fnamee = Entry(frame2, font='Arial  12', bg='white', fg='black')
        fnamee.place(x=180, y=130)
        dob = Label(frame2, text='Date Of Birth', font='Arial  12', bg='black', fg='white', width=16)
        dob.place(x=20, y=190)
        dobe = DateEntry(frame2, width=27, bg="darkblue", fg="white", year=2020)
        dobe.place(x=180, y=190)
        qualif = Label(frame2, text='Qualification', font='Arial  12', bg='black', fg='white', width=16)
        qualif.place(x=20, y=250)
        qualife = Entry(frame2, font='Arial  12', bg='white', fg='black')
        qualife.place(x=180, y=250)
        gender = Label(frame2, text='Gender', font='Arial  12', bg='black', fg='white', width=16)
        gender.place(x=20, y=310)
        radio = IntVar()
        R1 = Radiobutton(frame2, text="Male", variable=radio, value=1)
        R1.place(x=180, y=310)
        R2 = Radiobutton(frame2, text="Female", variable=radio, value=2)
        R2.place(x=250, y=310)
        R3 = Radiobutton(frame2, text="Other", variable=radio, value=3)
        R3.place(x=330, y=310)

        email = Label(frame2, text='Email', font='Arial  12', bg='black', fg='white', width=16)
        email.place(x=20, y=380)
        # email.bind("<Button>",check)
        emaile = Entry(frame2, font='Arial  12', bg='white', fg='black')
        emaile.place(x=180, y=380)
        number = Label(frame2, text='Contact Number', font='Arial  12', bg='black', fg='white', width=16)
        number.place(x=20, y=440)
        numbere = Entry(frame2, font='Arial  12', bg='white', fg='black')
        numbere.place(x=180, y=440)

        adrs = Label(frame2, text='Address', font='Arial  12', bg='black', fg='white', width=16)
        adrs.place(x=800, y=70)
        adrse = Entry(frame2, font='Arial  12', bg='white', fg='black', width=40)
        adrse.place(x=800, y=100)
        streetadrs = Label(frame2, text='Street Address', font='Arial  8', bg='black', fg='white', width=16)
        streetadrs.place(x=800, y=122)
        adrse2 = Entry(frame2, font='Arial  12', bg='white', fg='black', width=40)
        adrse2.place(x=800, y=150)
        streetadrs2 = Label(frame2, text='Street Address 2', font='Arial  8', bg='black', fg='white', width=16)
        streetadrs2.place(x=800, y=172)
        city = Entry(frame2, font='Arial  12', bg='white', fg='black', width=18)
        city.place(x=800, y=210)
        cityl = Label(frame2, text='City', font='Arial  8', bg='black', fg='white', width=16)
        cityl.place(x=800, y=232)
        state = Entry(frame2, font='Arial  12', bg='white', fg='black', width=18)
        state.place(x=1000, y=210)
        statel = Label(frame2, text='State', font='Arial  8', bg='black', fg='white', width=16)
        statel.place(x=1000, y=232)
        pin = Entry(frame2, font='Arial  12', bg='white', fg='black', width=18)
        pin.place(x=800, y=270)
        pinl = Label(frame2, text='Postal / Zip Code', font='Arial  8', bg='black', fg='white', width=16)
        pinl.place(x=800, y=292)

        try:
            mydb1 = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur1 = mydb1.cursor()
            try:
                cur1.execute("select * from studreg")
                str = cur1.fetchall()
                x = len(str)
                x += 1
                ide.insert(0, x)
                ide.configure(state='disabled')
            except:
                mydb1.rollback()
        except:
            print('n')
        amount1 = Label(frame2, text='Amount have to pay', font='Arial  12', bg='black', fg='white', width=16)
        amount1.place(x=800, y=340)
        amounte1= Entry(frame2, font='Arial  12', bg='white', fg='black', width=15)
        amounte1.place(x=980, y=340)
        amount2 = Label(frame2, text='Amount Paid', font='Arial  12', bg='black', fg='white', width=16)
        amount2.place(x=800, y=400)
        amounte2 = Entry(frame2, font='Arial  12', bg='white', fg='black', width=15)
        amounte2.place(x=980, y=400)



#Frame1111/////////////////////////////////////////////////

        global nameec, fnameec, numberec, bed1, htype, aaa, o1, o2, o3, o4, o5
        frame = Frame(img, width=1200,height=600, borderwidth=5,bg='black',highlightcolor="red", highlightthickness=1)
        frame.place(x=80, y=80)
        load3= Image.open("F:/image/2.jpg")
        load3 = load3.resize((1192, 594), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(frame, image=render3,bg='black')
        img3.image = render3
        img3.place(x=-5, y=-5)

        id1 = Label(frame, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id1.place(x=10, y=10)
        ide1 = Entry(frame, width=5, font='Arial  12', bg='white', fg='black')
        ide1.place(x=80, y=10)
        ide1.insert(0, x)
        ide1.configure(state='disabled')

        l = Label(frame, text='Please Enter Below Details', font='Algerian  25  ', bg='black', fg='firebrick', cursor='hand2')
        l.place(x=340, y=-5)
        l1=Label(frame,text='Select Bed Type',font='Algerian  16  ',bg='black',fg='firebrick',cursor='hand2',width=28)
        l1.place(x=0,y=50)
        radio1 = IntVar()
        R1 = Radiobutton(img3, text="Single Bed Room", variable=radio1, value=1,bg='black',fg='firebrick',height=2)
        R1.place(x=20, y=80)
        R2 = Radiobutton(img3, text="Double Sharing", variable=radio1, value=2,bg='black',fg='firebrick',height=2)
        R2.place(x=150, y=80)
        R3 = Radiobutton(img3, text="Triple Sharing", variable=radio1, value=3,bg='black',fg='firebrick',height=2)
        R3.place(x=272, y=80)

        l2 = Label(img3, text='Select Payment Mode', font='Algerian  16  ', bg='black', fg='firebrick',width=28)
        l2.place(x=0, y=180)
        radio2 = IntVar()
        R4 = Radiobutton(img3, text="Monthly", variable=radio2, value=1, bg='black', fg='firebrick',height=2,width=10)
        R4.place(x=20, y=210)
        R5= Radiobutton(img3, text="Quaterly", variable=radio2, value=2, bg='black', fg='firebrick',height=2,width=10)
        R5.place(x=150, y=210)
        R6 = Radiobutton(img3, text="Yearly", variable=radio2, value=3, bg='black', fg='firebrick',height=2,width=10)
        R6.place(x=272, y=210)

        l3 = Label(img3, text='Hostel Type', font='Algerian  16  ', bg='black', fg='firebrick',width=28)
        l3.place(x=0, y=320)
        radio3 = IntVar()
        R7 = Radiobutton(img3, text="Girls Hostel", variable=radio3, value=1, bg='black', fg='firebrick', height=2,width=15)
        R7.place(x=50, y=350)
        R8 = Radiobutton(img3, text="Boys Hostel", variable=radio3, value=2, bg='black', fg='firebrick', height=2,width=15)
        R8.place(x=237, y=350)

        l4 = Label(img3, text='Other Hostel Facilities', font='Algerian  16  ', bg='black', fg='firebrick',width=30)
        l4.place(x=800, y=50)
        checkvar1 = IntVar()
        checkvar2 = IntVar()
        checkvar3 = IntVar()
        checkvar4 = IntVar()
        checkvar5 = IntVar()
        chkbtn1 = Checkbutton(img3, text="GYM Facility", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=12, bg='black', fg='firebrick')
        chkbtn2 = Checkbutton(img3, text="Sports", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=12, bg='black', fg='firebrick')
        chkbtn3 = Checkbutton(img3, text="Mess", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=12, bg='black', fg='firebrick')
        chkbtn4 = Checkbutton(img3, text="Transportation", variable=checkvar4, onvalue=1, offvalue=0, height=2, width=12, bg='black', fg='firebrick')
        chkbtn5 = Checkbutton(img3, text="Internet", variable=checkvar5, onvalue=1, offvalue=0, height=2, width=12, bg='black', fg='firebrick')
        chkbtn1.place(x=800,y=100)
        chkbtn2.place(x=800,y=150)
        chkbtn3.place(x=800,y=200)
        chkbtn4.place(x=800, y=250)
        chkbtn5.place(x=800, y=300)
        def dialogfile(self):
            global path, img4

            path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
            load4 = Image.open(path)
            load4 = load4.resize((120, 120), Image.ANTIALIAS)
            render4 = ImageTk.PhotoImage(load4)
            img4 = Label(frame2, image=render4,width=120,height=120)
            img4.image = render4
            img4.place(x=510, y=40)

        imageb=Button(frame2,text='Choose File',width=20,cursor='hand2')
        imageb.place(x=500,y=200)
        imageb.bind('<Button>',dialogfile)



        try:
            global b11,g11
            mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur1 = mydb.cursor()
            cur1.execute("select * from room")
            rec1 = cur1.fetchall()
            for xx in rec1:
                bb11=int(xx[0])
                gg11=int(xx[1])
                b11=int(xx[2])
                g11=int(xx[3])
                print('s')
        except:
            print('d')

        def dialogfile1():
            if (radio3.get() == 1):
                girl = g11 - 1
                girl1=gg11+1
            else:
                girl=g11
                girl1=gg11

            if (radio3.get() == 2):
                boy = b11 - 1
                boy1=bb11+1
            else:
                boy=b11
                boy1=bb11
            print(girl)
            print(boy)
            mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur = mydb.cursor()
            sql3 = "update room set boyroom=%s,girlroom=%s, totalboyr=%s,totalgirlr=%s"
            val = (boy1,girl1,boy,girl)
            cur.execute(sql3, val)
            mydb.commit()


        def frame2_open():
            if (radio1.get() == 0):
                messagebox.showinfo('message', 'Please select bed type')
            elif (radio2.get() == 0):
                messagebox.showinfo('message', 'Please select payment mode')
            elif (radio3.get() == 0):
                messagebox.showinfo('message', 'Please select hostel type')
            else:
                frame.destroy()
                if (radio1.get() == 1):
                    bed = 3000
                elif (radio1.get() == 2):
                    bed = 2000
                elif (radio1.get() == 3):
                    bed = 1000
                if (radio3.get() == 1):
                    htype=6000
                elif (radio3.get() == 2):
                    htype=5000

                if (checkvar1.get() == 1):
                    o1=1000
                else:
                    o1=0
                if (checkvar2.get() == 1):
                    o2=1000
                else:
                    o2=0

                if (checkvar3.get() == 1):
                    o3=1000
                else:
                    o3=0

                if (checkvar4.get() == 1):
                    o4=1000
                else:
                    o4=0

                if (checkvar5.get() == 1):
                    o5=1000
                else:
                    o5=0


                aaa=bed+htype+o1+o2+o3+o4+o5
                amounte1.insert(0,aaa)
                amounte1.configure(state='disabled')
                frame2.place(x=80, y=80)
                img1.destroy()




        def connect():
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

            nameec = namee.get()
            fnameec = fnamee.get()
            numberec = numbere.get()
            email = emaile.get()

            if not nameec.isalpha() or nameec in "'-":
                messagebox.showerror('message', 'Please Enter Valid Name')
            elif not fnameec.isalpha() or fnameec in "":
                messagebox.showerror('message', 'Please Enter Father Name')
            elif (dobe.get() == ''):
                messagebox.showerror('message', 'Please Enter Date of Birth')
            elif (qualife.get() == ''):
                print(qualife.get())
                messagebox.showerror('message', 'Please Enter Qualification Details')
            elif (email == ''):
                messagebox.showerror('message', 'Please Enter Valid Email Details')
            elif len(numberec) < 10 or len(numberec) > 10 or not (numberec.isdigit()):
                messagebox.showerror('message', '* Must be 10-digit phone number without spaces')
            elif (path==''):
                messagebox.showerror('message', '* Must be 10-digit phone number without spaces')

            else:
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                sql = "insert into studreg(id,name,fname, dob,qualif, gender,email,number,address,streetadrss,city,state,pin,amounthvtopay,paidamount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)"

                a = ide.get()
                b = namee.get()
                c = fnamee.get()
                d = dobe.get()
                e = qualife.get()
                if (radio.get() == 1):
                    f = "Male"
                elif (radio.get() == 2):
                    f = "Female"
                elif (radio.get() == 3):
                    f = "other"
                g = emaile.get()
                h = numbere.get()
                i = adrse.get()
                j = adrse2.get()
                k = city.get()
                l = state.get()
                m = pin.get()
                k1 = int(amounte2.get())
                kk1 = int(amounte1.get())
                n = kk1 - k1
                o=amounte2.get()
                value1 = (a, b, c, d, e, f, g, h, i, j, k, l, m,n,o)
#second//////////////////////
                sql1 = "insert into  fasility(id,bedtype,payment,roomtype,gym,sports,mess,transport,internet) values (%s,%s,%s,%s,%s,%s,%s,%s, %s)"

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
                    boy = b11 - 1
                    print(boy)
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

                value2 = (a, a1, b1, c1, d1, e1, f1, g1, h1)
                print(value2)
                print(value1)


                with open(path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())

                sql2 = 'INSERT INTO pic VALUES(%s,%s)'
                args = (a,encoded_string)

                try:
                    cur.execute(sql, value1)
                    cur.execute(sql1, value2)
                    cursor = mydb.cursor()
                    cursor.execute(sql2, args)

                    mydb.commit()
                    messagebox.showinfo('message', 'inserted')
                except:
                    mydb.rollback()

                mydb.close()
                root.destroy()
                Createpw.Createpw()

        submit = Button(frame2, text="Submit",command=lambda:[dialogfile1(),connect()])
        submit.place(x=500, y=500)
        #submit.bind('<Button>', connect)



        b=Button(frame,text='Proceed',command=frame2_open,width=15, font='Algerian  ', bg='black', fg='firebrick')
        b.place(x=1000,y=500)

        root.mainloop()
#Selection()