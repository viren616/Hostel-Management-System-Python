from tkinter import *
from tkinter import messagebox
import time

Freq = 2500
Dur = 150

top = Tk()
top.title('MapAwareness')
top.geometry('200x100') # Size 200, 200
image_files = [
    'E:/prog/qp/1.png',
    'E:/prog/qp/2.png',
    'E:/prog/qp/5.png',
    'E:/prog/qp/a.png',
    'E:/prog/qp/aa.png'
]


def start():
    i=0
    print (image_files)
    time.sleep(1)
    top.after(len(image_files[i]), start)
    i=i+1
def stop():
    print ("Stop")
    top.quit()

startButton = Button(top, height=2, width=20, text ="Start", command = start)
stopButton = Button(top, height=2, width=20, text ="Stop", command = stop)

startButton.pack()
stopButton.pack()
top.mainloop()


def proceeed():
    global id
    id = usere.get()

    if (usere.get() == '' or passwe.get() == ''):
        messagebox.showinfo('message', 'please fill the details')
    else:
        f = 0
        mydb = mysql.connector.connect(host='localhost', user='root', password='viren', database='python')
        cur = mydb.cursor()
        cur.execute("select * from password")
        rec = cur.fetchall()
        for x in rec:
            if (usere.get() == x[0]):
                if (passwe.get() == x[1]):
                    f = 1
                    break
        if (f == 1):
            frame1.destroy()
            frame.place(x=80, y=80)
            ide.insert(0, id)
            ide.configure(state='disabled')

        else:
            messagebox.showinfo('message', 'Invalid user')
