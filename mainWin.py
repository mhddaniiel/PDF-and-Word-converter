from tkinter import *

def openWordfile():
    pass

def openImagefile():
    pass

files = {}
def openImagefile():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')])

    img_list = []

    for file in files['filename']:
        img_list.append(Image.open(file).convert('RGB'))
        img_list.append
        
    save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')])
    img_list[0].save(f'{save_file_name}.pdf', save_all = True, append_images = img_list[1:])



window = Tk()
window.title("Words & Images to PDF Converter (Student Edition)")
window.geometry('450x200')

Word_butt=Button(window, text="Select Word Files", width=30, command=openWordfile)
Word_butt.grid(row =2, column = 0, padx=120, pady =20) 

Img_butt=Button(window, text="Select Image Files", width=30, command=openImagefile)
Img_butt.grid(row =3, column = 0, padx=120, pady =20)    

window.mainloop()