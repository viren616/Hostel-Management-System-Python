from tkinter import *
from itertools import cycle
import threading
import time
from PIL import ImageTk,Image
import Adminlogin
import Payment
import Selection
class Home():
    def __init__(self):
        root= Tk()
        root.geometry('1369x769+0+0')
        root.overrideredirect(True)
        root.lift()
        root.attributes("-topmost",True)

        load=Image.open("E:/prog/qp/50c.jpg")
        load=load.resize((1373,773),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img=Label(root, image=render)
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
        img2 = Label(border, image=render2, bg='black', cursor='hand2')
        img2.image = render2
        img2.place(x=1140, y=0)
        img2.bind("<Button>", close)

        b1=Button(frame,text="Home",width=32,bg='black', fg='firebrick',activebackground='firebrick',activeforeground='white',cursor='hand2')
        b1.place(x=0,y=80)

        def adminlogin(event):
            root.destroy();
            Adminlogin.Adminlogin();

        b2=Button(frame,text="Admin Login",width=32,bg='black', fg='firebrick',activebackground='firebrick',activeforeground='black',cursor='hand2')
        b2.place(x=227,y=80)
        b2.bind("<Button>", adminlogin)

        def reg(event):
            root.destroy();
            Selection.Selection()
        b3 = Button(frame, text="Registration", width=32,bg='black', fg='firebrick',activebackground='firebrick',activeforeground='black',cursor='hand2')
        b3.place(x=461, y=80)
        b3.bind("<Button>", reg)

        def payment(event):
            root.destroy();
            Payment.Payment()
        b4 = Button(frame, text="Payemnt", width=34,bg='black', fg='firebrick',activebackground='firebrick',activeforeground='black',cursor='hand2')
        b4.place(x=695, y=80)
        b4.bind("<Button>", payment)

        b5 = Button(frame, text="About", width=34,bg='black', fg='firebrick',activebackground='firebrick',activeforeground='black',cursor='hand2')
        b5.place(x=943, y=80)


        image_files = [
            'E:/prog/p/h.jpg',
            'E:/prog/p/normal_5.jpg',
            'E:/prog/p/hhhh.jpg',
            'E:/prog/p/mess.jpg',
            'E:/prog/p/room.jpg'
        ]
        def loop1_10():
            i = 0
            while i >= 0:
                time.sleep(1)
                i = i + 1
                if(i==5):
                    i=0
                print(image_files[i])
                loads = Image.open(image_files[i])
                loads = loads.resize((350, 350), Image.ANTIALIAS)
                renders = ImageTk.PhotoImage(loads)
                imgs = Label(frame, image=renders,borderwidth=0)
                imgs.image = renders
                imgs.place(x=410, y=200)

        threading.Thread(target=loop1_10).start()

        root.mainloop()


#app = Home()

