from tkinter import*
from PIL import ImageTk,Image

root=Tk()
root.resizable("False","False")
root.title("Photo View pro")

im1 = ImageTk.PhotoImage(Image.open(r"D:\adobe raw\im1.jpg"))
im2 = ImageTk.PhotoImage(Image.open(r"D:\adobe raw\im2.jpg"))
im3 = ImageTk.PhotoImage(Image.open(r"D:\adobe raw\im4.jpg"))

image_list = [im1,im2,im3]

def forword(image_number):
     global l1
     global b1
     global b3
     l1.grid_forget()
     l1 = Label(image=image_list[image_number-1])
     b3 = Button(root,text=">>",command=lambda:forword(image_number+1)) 
     b3.grid(row=1,column=2)
     b1 = Button(root,text="<<",command=lambda:back(image_number-1))
     b1.grid(row=1,column=0)

     l1.grid(row=0,column=0,columnspan=3)
     


def back(image_number):
    global l1
    global b1
    global b3
    l1.grid_forget()
    l1 = Label(image=image_list[image_number-1])
    b3 = Button(root,text=">>",command=lambda:forword(image_number+1)) 
    b3.grid(row=1,column=2)
    b1 = Button(root,text="<<",command=lambda:back(image_number-1))
    b1.grid(row=1,column=0)

    l1.grid(row=0,column=0,columnspan=3)


l1 =Label(image=im1)
l1.grid(row=0,column=0,columnspan=3)

b1 = Button(root,text="<<",command=back)
b2 = Button(root,text="Exit",command=quit)
b3 = Button(root,text=">>",command=lambda:forword(2))

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)



root.mainloop()
