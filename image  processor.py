import tkinter as tk
import tkinter.messagebox
import threading
from tkinter import *
from tkinter import filedialog
from pil import Image, ImageFilter, ImageTk, ImageDraw
from tkinter import Tk, Frame, Button, BOTH, SUNKEN, colorchooser
import os
import numpy as np
from pil import Image, ImageEnhance
from tkinter.ttk import *
#from time import strftime
import cv2

root = tk.Tk()
root.config(background='red')
# tk.background('red')
# global panel= NONE
panel = None
panelA = None
panelB = None

###############
# style configuration

###############

frame = tk.Frame(root, width=50, height=1000, bg="lightgrey")
frame.pack(side="left")
frame1 = tk.Frame(root, width=50, height=900, bg="grey")
frame1.pack(side="right")
frame2 = tk.Frame(root, width=1400, height=20, bg="grey")
frame2.pack(side="top")

# scale
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
   
def open12():
    import tkinter.filedialog as qw
    root.withdraw()
    file_path = qw.askopenfilename()

def open():
        fileName = tk.getOpenFileName(tk,'openFile')
        tk.address.setText(fileName[0])
        tk.showImage(fileName[0])
        # print(fileName)
# Create a Grayscale version of the image
def open_img():
    global panel
    x = openfn()
    img = Image.open(x)
    img = img.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel = Label(root, image=img)
    panel.image = img
    
    #panel.image = NONE
    panel.pack(side="top", fill="both", expand="NO")    
def exit():
    
    #panel = Label(root, '')
    panel.destroy()
    #panel.pack(side="top", fill="both", expand="NO")    
    # root.image.blank()
    # root.image = ''
    # panel = Label(root, image=img)
    #panel.image = NONE
    # panel.pack(side="top", fill="both", expand="NO")   

def contrast():
    global panel
    x = openfn()
    im = Image.open(x) 
    im3 = ImageEnhance.Contrast(im)
    im2 = im3.enhance(2.0)
    img = im2.resize((1000, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    #panel.image = NONE   
    
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            im3.enhance(2.0).save("contrast.jpg")
    
    threading.Timer(5.0,saveb).start()
root.title('acura 2.0') 
  
 

  
# canvas = Canvas(height=200,width=2 00)
# canvas.pack()   
# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack() 
# import openauto


#def select_image():
#      import openauto

def blur():
    global panel
    x = openfn()
    img = Image.open(x)
    im = img.filter(ImageFilter.BLUR)
    img = im.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel = Label(root, image=img)
    panel.image = img
    #panel.image = NONE
    panel.pack(side="top", fill="both", expand="NO")    
    
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            im.save('blur.jpg')
        
    
    threading.Timer(5.0,saveb).start()
    # im.show()
def abhi():
    import tkinter as qw
    root=qw.Tk()
    im = Image.open(
    'F:\wallpaper\Wallpaperz\arizona_waterfalls-wide.jpg')
    # im = im.resize((950, 1050))
    # img = ImageTk.PhotoImage(Image.open('F:\wallpaper\Wallpaperz\arizona_waterfalls-wide.jpg'))
    panel = Label(root, image = im)
    panel.pack(side = "bottom", fill = "both", expand = "yes") 
    root.mainloop()   
# Invoking through button
def blackwhite():
    global panel
    x = openfn()
    color_image = Image.open(x)
    bw = color_image.convert('L')
    img = bw.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")
    
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            bw.save('blackandwhite.jpg')
       
    
    threading.Timer(5.0,saveb).start()

def color123():
    pick=colorchooser.askcolor(title="select color")
    print (pick)  
def gradient():
    global panel
    
    
    img = Image.new('RGB', (300, 200), (150, 150, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((100,100, 150, 100), fill=(255, 120,232 ))
    draw.ellipse((25, 25, 75, 75), fill=(255, 110, 0))
    #img.save('test.gif', 'GIF', transparency=0)
    img = img.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")

          
def colorfilter():
    global panel
    x = openfn()
    u = color123()
    color_image = Image.open(x)
    bw = color_image.convert('L')
    img = bw.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")    
def input():
    print("enter the file name")  
    from inputproject import wq
    qw=wq
    print(qw)
    im = Image.open(qw,"r")
    im.show()  
def brightness():
    global panel
    x = openfn()
    im = Image.open(x) 
    im3 = ImageEnhance.Brightness(im)
    im2 = im3.enhance(2.0)
    img = im2.resize((1000, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    #panel.image = NONE   
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            im3.enhance(2.0).save("brightness.jpg")
            
    threading.Timer(5.0,saveb).start()
     
    
    # Creating object of Brightness class 
     
    
    # showing resultant image 
    
# def helloCallBack():
#   messagebox.showinfo("quit", "are you sure you want to quit")
#  close_window(root)
def sharpen():
    global panel
    x = openfn()
    im = Image.open(x)
    im_sharp = im.filter(ImageFilter.SHARPEN)
    img = im_sharp.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")
    #im_sharp.save('image_sharpened.jpg', 'JPEG')
    #im_sharp.show()
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            im_sharp.save('sharpen.jpg')
        
    
    threading.Timer(5.0,saveb).start()

def cropy():
    global panel
    x = openfn()
    image_obj = Image.open(x)
    cropped_image = image_obj.crop((161, 166, 706, 1050))
    img = cropped_image.resize((400,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            cropped_image.save('crop.JPEG')
        
    
    threading.Timer(5.0,saveb).start()
    #cropped_image.save('hello.JPEG')
    #cropped_image.show()
# def close_window(root):
#   root.destroy()
def camera():
    cap = cv2.VideoCapture(0)
    img_counter = 0
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        def apply_invert(frame):
            return cv2.bitwise_not(frame)
        lower_red = np.array([30, 150, 50])
        upper_red = np.array([255, 255, 180])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        invert=apply_invert(frame)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        cv2.imshow('invert', invert)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1    
    cv2.destroyAllWindows()
    cap.release()

    

def rotate():
    global panel
    x = openfn()
    image_obj = Image.open(x)
    rotated_image = image_obj.rotate(90)
    img = rotated_image.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")
    #rotated_image.save(saved_location)
    #rotated_image.show()
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            rotated_image.save('rotate.JPEG')
        
    
    threading.Timer(5.0,saveb).start()
def mirror():
    global panel
    x = openfn()
    image_obj = Image.open(x)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    img = rotated_image.resize((1250, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side="top", fill="both", expand="NO")
    def saveb():
        MsgBox = tk.messagebox.askquestion(
            'SAVE', 'do you want to save the img', icon='warning')
        if MsgBox == 'yes':
            rotated_image.save('mirror.JPEG')
        
    
    threading.Timer(5.0,saveb).start()

    #rotated_image.save(saved_location)
    #rotated_image.show()    
def ExitApplication():
    MsgBox = tk.messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo(
            'Return', 'You will now return to the application screen')

    

# power button
button = tk.Button(frame,
                   text="blackwhite",
                   bg= "dark grey",
                   command= blackwhite,
                   height=3,width=10)
button.config(height=1, width=2)
button.pack(side="top", expand=True, padx=4, pady=4)
# endof power button

# button 1
button1 = tk.Button(frame,
                   text="rotate",
                   bg = "darkgrey",
                   height=3,width=10,
                   command=rotate
                   )
button1.config(height=100, width=2)
button1.pack(side="bottom", padx=1, pady=2)
# end of button1

# button2
button2 = tk.Button(frame,
                   text="blur",
                   bg="darkgrey",
                   command=blur,
                   height=3,width=10)
button2.config(height=1, width=2)
button2.pack(side="bottom", padx=1, pady=2)
# endbutton2

# button3
button3 = tk.Button(frame,
                   text="brightness",
                   bg="darkgrey",
                   command=brightness,
                   height=3,width=10)
button3.config(height=1, width=2)
button3.pack(side="bottom", padx=1, pady=2)
# endbutton3

# button4
button4 = tk.Button(frame,
                   text="crop",
                   bg="darkgrey",
                   command=cropy,
                   height=3,width=10)
button4.config(height=1, width=2)
button4.pack(side="bottom", padx=1, pady=2)

# endbutton4

# button5
button5 = tk.Button(frame,
                   text="Colorpicker",
                   bg="darkgrey",
                   command=color123,
                   height=3,width=10)
button5.config(height=1, width=2)
button5.pack(side="bottom", padx=1, pady=2)

# endbutton5

# button6
button6 = tk.Button(frame,
                   text="mirror",
                   bg="darkgrey",
                   command=mirror,
                   height=3,width=10)
button6.config(height=1, width=2)
button6.pack(side="bottom", padx=1, pady=2)

# endbutton6
btn = tk.Button(root, text='open image', command=open_img).pack(side="top", padx=1, pady=2)
btn2 = Button(root, text='clear image', command=exit).pack()
# button7
button7 = tk.Button(frame,
                   text="camera",
                   bg="darkgrey",
                   command=camera,
                   height=3,width=10)
button7.config(height=1, width=2)
button7.pack(side="bottom", padx=1, pady=2)

# endbutton7

# button8
button8 = tk.Button(frame,
                   text="sharp",
                   bg="darkgrey",
                   command=sharpen,
                   height=3,width=10)
button8.config(height=1, width=2)
# button8.grid(row=0, column=0)
# button8.place(x=0, y=0, width=120, height=25)
button8.pack(side="bottom", padx=1, pady=2)

# endbutton8
button9 = tk.Button(frame,
                   text="cont",
                   bg="darkgrey",
                   command=contrast,
                   height=3,width=10)
button9.config(height=1, width=2)
# button8.grid(row=0, column=0)
# button8.place(x=0, y=0, width=120, height=25)
button9.pack(side="bottom", padx=1, pady=2)

# button10 = tk.Button(frame,
#                    text="paint",
#                    bg="darkgrey",
#                    command=paint,
#                    height=3,width=10)
# button10.config(height=1, width=2)
# # button8.grid(row=0, column=0)
# # button8.place(x=0, y=0, width=120, height=25)
# button10.pack(side="bottom", padx=1, pady=2)

# canvas1.create_window(150, 150, window=button)
# im_sharp.save('image_sharpened.jpg', 'JPEG')
button11 = tk.Button(frame,
                   text="gradient",
                   bg="darkgrey",
                   command=gradient,
                   height=3,width=10)
button11.config(height=1, width=2)
# button8.grid(row=0, column=0)
# button8.place(x=0, y=0, width=120, height=25)
button11.pack(side="bottom", padx=1, pady=2)


#img = ImageTk.PhotoImage(im)
#panel = Label(root, image=img)
#panel.pack(side="top", fill="both", expand="NO")

# button8.grid(row=0, column=0)
# button8.place(x=0, y=0, width=120, height=25)
button11.pack(side="bottom", padx=1, pady=2)

root.protocol('WM_DELETE_WINDOW', ExitApplication)  # root is your root window
root.iconbitmap(r'F:\Icos\Camera.ico')
root.mainloop()
