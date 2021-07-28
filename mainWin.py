#Built-in plugIn
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Install plugIn
from PIL import Image
from docx2pdf import convert

#Word & Image to PDF Window
def win2():
    global files, back_img, butt_word, butt_img

    def openWordfile():
        file = filedialog.askopenfile(filetypes=[('Word', '*.docx')])
        convert(file.name)

        messagebox.showinfo(title='Announcement', message='The PDF files stored under the WORD file you converted')

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

        messagebox.showinfo(title='Announcement', message='The PDF file is stored at a place of your choice')

    window=Toplevel(main)
    window.title("Words & Images to PDF Converter (Student Edition)")
    window.geometry('500x500+520+100')
    window.iconbitmap(r'icon.ico')
    window.resizable(0,0)

    back_img = PhotoImage(file='canvas.png')
    img_back = Label(window, image=back_img)
    img_back.place(relwidth=1, relheight=1)

    menuBar = Menu(window)
    window.config(menu=menuBar)

    checkMenu = Menu(menuBar)
    menuBar.add_cascade(label='Menu', menu=checkMenu)
    checkMenu.add_command(label='Quit', command=window.destroy)

    butt_word = PhotoImage(file='wordButton.png')
    Word_butt=Button(window, image=butt_word, width=100, height=50, borderwidth=0, command=openWordfile)
    Word_butt.place(relx=0.48,rely=0.86) 

    butt_img = PhotoImage(file='imageButton.png')
    Img_butt=Button(window, image=butt_img, width=100, height=50, borderwidth=0, command=openImagefile)
    Img_butt.place(relx=0.7,rely=0.86)   

def win3():
    pass

#mainWindow
main = Tk()
main.resizable(0,0)
main.geometry('300x100')
main.title('Option Window')
main.iconbitmap('icon.ico')

mainButt1 = Button(main, text='Enter Word & Image to PDF Window', command=win2)
mainButt1.pack()

mainButt2 = Button(main, text='Enter Student Assignment Recorder Window', command=win3)
mainButt2.pack()

main.mainloop()