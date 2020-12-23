from tkinter import *
import threading
import time
from tkinter import*
from PIL import Image,ImageTk
from tkinter import Tk

class Cr:
   def __init__(self):
      root=Tk()
      root.geometry('1200x600')
      f=0

      frame = Frame(root, bg='gray', width=300, height=400)
      frame.place(x=100, y=20)
      checkvar1 = IntVar()
      chkbtn1 = Checkbutton(root, text="GYM Facility", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=12, bg='black', fg='firebrick')
      print(checkvar1.get())
      image_files = [
          'E:/prog/qp/1.png',
          'E:/prog/qp/2.png',
          'E:/prog/qp/5.png',
          'E:/prog/qp/a.png',
          'E:/prog/qp/aa.png'
      ]
      def loop1_10():
         try:
            global i
            i=0
            for i in range(len(image_files)):
                if(i>=len(image_files)):
                    i=0
                time.sleep(.500)
                i = i + 1
                print(i)
         except:
             print('r')

      threading.Thread(target=loop1_10).start()


      root.mainloop()

Cr()


