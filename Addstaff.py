from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
from tkinter import filedialog
from tkinter import messagebox
import Staffpass
import Staff
class Addstaff:
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
        label1=Label(img,text='Add Staff',font='Arial  25  bold', bg='black', fg='white',width=60)
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


        frame = Frame(img, width=1200, height=600, borderwidth=5)
        frame.place(x=80, y=80)
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
            img4 = Label(frame, image=render4,width=120,height=120)
            img4.image = render4
            img4.place(x=510, y=40)


        b=Button(frame,text='Choose File',width=20,cursor='hand2')
        b.place(x=500,y=200)
        b.bind('<Button>',dialogfile)


        id = Label(img1, text='ID no.', font='Arial  12', bg='black', fg='white', width=5)
        id.place(x=10, y=10)
        ide = Entry(img1, width=5, font='Arial  12', bg='white', fg='black')
        ide.place(x=80, y=10)

        name=Label(img1,text='Enter Name',font='Arial  12', bg='black', fg='white',width=13)
        name.place(x=20,y=70)
        namee=Entry(img1,font='Arial  12', bg='white', fg='black')
        namee.place(x=180,y=70)
        fname = Label(img1, text='Enter Father Name', font='Arial  12', bg='black', fg='white', width=16)
        fname.place(x=20, y=130)
        fnamee = Entry(img1, font='Arial  12', bg='white', fg='black')
        fnamee.place(x=180, y=130)
        dob = Label(img1, text='Date Of Birth', font='Arial  12', bg='black', fg='white', width=16)
        dob.place(x=20, y=190)
        dobe = DateEntry(img1, width=27, bg="darkblue", fg="white", year=2020)
        dobe.place(x=180, y=190)
        qualif = Label(img1, text='Qualification', font='Arial  12', bg='black', fg='white', width=16)
        qualif.place(x=20, y=250)
        qualife = Entry(img1, font='Arial  12', bg='white', fg='black')
        qualife.place(x=180, y=250)
        gender = Label(img1, text='Gender', font='Arial  12', bg='black', fg='white', width=16)
        gender.place(x=20, y=310)
        radio = IntVar()
        R1 = Radiobutton(img1, text="Male", variable=radio, value=1)
        R1.place(x=180,y=310)
        R2 = Radiobutton(img1, text="Female", variable=radio, value=2)
        R2.place(x=250,y=310)
        R3 = Radiobutton(img1, text="Other", variable=radio, value=3)
        R3.place(x=330,y=310)

        email = Label(img1, text='Email', font='Arial  12', bg='black', fg='white', width=16)
        email.place(x=20, y=380)
        #email.bind("<Button>",check)
        emaile = Entry(img1, font='Arial  12', bg='white', fg='black')
        emaile.place(x=180, y=380)
        number = Label(img1, text='Contact Number', font='Arial  12', bg='black', fg='white', width=16)
        number.place(x=20, y=440)
        numbere = Entry(img1, font='Arial  12', bg='white', fg='black')
        numbere.place(x=180, y=440)

        adrs = Label(img1, text='Address', font='Arial  12', bg='black', fg='white', width=16)
        adrs.place(x=800, y=70)
        adrse = Entry(img1,font='Arial  12', bg='white', fg='black',width=40)
        adrse.place(x=800, y=100)
        streetadrs = Label(img1, text='Street Address', font='Arial  8', bg='black', fg='white', width=16)
        streetadrs.place(x=800, y=122)
        adrse2 = Entry(img1,font='Arial  12', bg='white', fg='black',width=40)
        adrse2.place(x=800, y=150)
        streetadrs2 = Label(img1, text='Street Address 2', font='Arial  8', bg='black', fg='white', width=16)
        streetadrs2.place(x=800, y=172)
        city = Entry(img1,font='Arial  12', bg='white', fg='black',width=18)
        city.place(x=800, y=210)
        cityl = Label(img1, text='City', font='Arial  8', bg='black', fg='white', width=16)
        cityl.place(x=800, y=232)
        state = Entry(img1, font='Arial  12', bg='white', fg='black', width=18)
        state.place(x=1000, y=210)
        statel = Label(img1, text='State', font='Arial  8', bg='black', fg='white', width=16)
        statel.place(x=1000, y=232)
        pin = Entry(img1, font='Arial  12', bg='white', fg='black', width=18)
        pin.place(x=800, y=270)
        pinl = Label(img1, text='Postal / Zip Code', font='Arial  8', bg='black', fg='white', width=16)
        pinl.place(x=800, y=292)

        try:
            mydb1 = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
            cur1 = mydb1.cursor()
            try:
                cur1.execute("select * from staffreg")
                str=cur1.fetchall()
                global x
                x=len(str)
                x+=1
                ide.insert(0,x)
                ide.configure(state='disabled')
            except:
                mydb1.rollback()
        except:
            print('n')

        def connect(event):
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            global nameec,fnameec,numberec
            nameec = namee.get()
            fnameec=fnamee.get()
            numberec = numbere.get()
            email = emaile.get()

            if not nameec.isalpha() or nameec in "'-" :
                messagebox.showerror('message', 'Please Enter Valid Name')
            elif not fnameec.isalpha() or fnameec in "":
                messagebox.showerror('message', 'Please Enter Father Name')
            elif (dobe.get()==''):
                messagebox.showerror('message', 'Please Enter Date of Birth')
            elif (qualife.get() == ''):
                print(qualife.get())
                messagebox.showerror('message', 'Please Enter Qualification Details')
            elif ( email==''):
                    messagebox.showerror('message', 'Please Enter Valid Email Details')
            elif len(numberec) < 10 or len(numberec)>10 or not(numberec.isdigit()):
                messagebox.showerror('message', '* Must be 10-digit phone number without spaces')
            else:
                mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
                cur = mydb.cursor()
                sql = "insert into staffreg(id,name,fname, dob,qualif, gender,email,number,adress,streetadrss,city,state,pin) values (%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)"
                a=ide.get()
                b=namee.get()
                c=fnamee.get()
                d=dobe.get()
                e=qualife.get()
                if (radio.get() == 1):
                    f = "Male"
                elif (radio.get() == 2):
                    f = "Female"
                elif (radio.get() == 3):
                    f = "other"
                g=emaile.get()
                h=numbere.get()
                i=adrse.get()
                j=adrse2.get()
                k=city.get()
                l=state.get()
                m=pin.get()
                value=(a,b,c,d,e,f,g,h,i,j,k,l,m)
                print(value)
                try:
                    cur.execute(sql, value)
                    mydb.commit()
                    messagebox.showinfo('message', 'inserted')
                except:
                    mydb.rollback()

                mydb.close()
                root.destroy()
                Staffpass.Staffpass()

        submit=Button(frame,text="Submit")
        submit.place(x=500,y=500)
        submit.bind('<Button>',connect)
        root.mainloop()
#Addstaff()