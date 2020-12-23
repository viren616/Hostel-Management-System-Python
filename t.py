from itertools import cycle
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
class App(Tk):
    def d(self,image_files, delay):

        self.geometry('1300x600+0+0')
        self.delay = delay
        self.pictures = cycle((PhotoImage(file=image), image)for image in image_files)
        self.picture_display = Label(self)
        self.picture_display.place(x=0,y=0)


    def show_slides(self):
        img_object, img_name = next(self.pictures)
        load = Image.open(img_name)
        load = load.resize((1300, 600), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label( image=render)
        img.image = render
        img.place(x=0, y=0)
        self.after(delay, self.show_slides)
        self.mainloop()
delay = 100
image_files = [
'E:/prog/qp/1.png',
'E:/prog/qp/2.png',
'E:/prog/qp/5.png',
'E:/prog/qp/a.png',
'E:/prog/qp/aa.png'
]

app = App()
app.d(image_files, delay)
app.show_slides()
