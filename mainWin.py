from tkinter import *
#To setup GUI canvas using python code.
window = Tk()
window.title("Words & Images to PDF Converter (Student Edition)")
window.geometry('450x200')

#To create Button at GUI
Word_butt=Button(window, text="Select Word Files", width=30)
Word_butt.grid(row =2, column = 0, padx=120, pady =20) 

Img_butt=Button(window, text="Select Image Files", width=30)
Img_butt.grid(row =3, column = 0, padx=120, pady =20)

window.mainloop()