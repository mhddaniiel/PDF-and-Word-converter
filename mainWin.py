#Built-in plugIn
import os
import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Installed plugIn
from PIL import Image
from docx2pdf import convert

#secondWindow
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

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinInitialization
    newWin=Toplevel(main)
    newWin.title("Words & Images to PDF Converter (Student Edition)")
    newWin.geometry('500x500+520+120')
    newWin.iconbitmap(r'icon.ico')
    newWin.resizable(0,0)

    back_img = PhotoImage(file='canvas.png')
    img_back = Label(newWin, image=back_img)
    img_back.place(relwidth=1, relheight=1)

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinMenubar
    menuBar = Menu(newWin)
    newWin.config(menu=menuBar)

    checkMenu = Menu(menuBar)
    menuBar.add_cascade(label='Menu', menu=checkMenu)
    checkMenu.add_command(label='Quit', command=newWin.destroy)

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinButtons
    butt_word = PhotoImage(file='wordButton.png')
    Word_butt=Button(newWin, image=butt_word, width=100, height=50, borderwidth=0, command=openWordfile)
    Word_butt.place(relx=0.48,rely=0.86) 

    butt_img = PhotoImage(file='imageButton.png')
    Img_butt=Button(newWin, image=butt_img, width=100, height=50, borderwidth=0, command=openImagefile)
    Img_butt.place(relx=0.7,rely=0.86)   

#thirdWindow
def win3():
    global back_img2,bd_img,b1_img,b2_img
    
    def openFile():
        global out
        file = filedialog.askopenfilename(filetypes=[('All Files', '*.*')])
        os.system('"%s"' % file)
        
        data = os.path.split(file)
        out=data[1]
        print(out)

    def buttDel():
        entry.delete(0,END)

    def ins():
        
        conn = sqlite3.connect('data-insert-here.db')
        c = conn.cursor()
        c.execute("INSERT INTO history(File,Mark) VALUES(?,?)",(entry.get(),out,))
        conn.commit()
        conn.close()

    def show():
        win4 = Toplevel(newWin)
        win4.title('DATABASE')
        win4.geometry('228x352+276+268')
        win4.iconbitmap(r'icon.ico')

        menuBar1 = Menu(win4)
        win4.config(menu=menuBar1)

        checkMenu1 = Menu(menuBar1)
        menuBar1.add_cascade(label='Maximize to see full', menu=checkMenu1)

        conn = sqlite3.connect('data-insert-here.db')
        c = conn.cursor()
        c.execute("SELECT * FROM history")
        conn.commit()

        records = c.fetchall()

        print_records1 = ''
        print_records2 = ''
        print_records3 = ''
        for r in records:
            #print_records1 += f'{str(r[0])}\t\t\t{str(r[2])}\t\t\t{str(r[1])}/100%\n'
            print_records1 += f'{str(r[0])}\n'
            print_records2 += f'{str(r[1])}/100%\n'
            print_records3 += f'{str(r[2])}\n'

        frame1 = LabelFrame(win4, text='Code', font=('Arial',10), bg='blue', fg='white')
        frame1.grid(row=0, column=0)
        lab1 = Label(frame1, text=print_records1)
        lab1.pack()

        frame2 = LabelFrame(win4, text='Mark', font=('Arial',10), bg='red', fg='white')
        frame2.grid(row=0, column=1)
        lab2 = Label(frame2, text=print_records2)
        lab2.pack()

        frame3 = LabelFrame(win4, text='File Name', font=('Arial',10), bg='green', fg='white')
        frame3.grid(row=0, column=2)
        lab3 = Label(frame3, text=print_records3)
        lab3.pack()
        
        conn.close()

    def delete():
        conn = sqlite3.connect('data-insert-here.db')
        c = conn.cursor()
        c.execute("DELETE from history")
        conn.commit()
        
        conn.close()

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinInitialization
    newWin = Toplevel(main)
    newWin.title('Student Assignment Recorder (Teacher Edition)')
    newWin.geometry('500x500+520+120')
    newWin.iconbitmap(r'icon.ico')
    newWin.resizable(0,0)

    back_img2 = PhotoImage(file='canvas2.png')
    img_back = Label(newWin, image=back_img2)
    img_back.place(relwidth=1, relheight=1)

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinMenubar
    menuBar = Menu(newWin)
    newWin.config(menu=menuBar)

    checkMenu = Menu(menuBar)
    menuBar.add_cascade(label='Database', menu=checkMenu)
    checkMenu.add_command(label='Delete Database', command=delete)
    checkMenu.add_command(label='Show Database', command=show)
    checkMenu.add_command(label='Quit', command=newWin.destroy)

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinEntry
    entry = Entry(newWin, borderwidth=0, font=('Times',14), justify='center')
    entry.place(x=298, y=346, relwidth=0.08, relheight=0.05)

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #newWinButtons
    delButt = Button(newWin, text='X', command=buttDel,  bg='#ff3847', fg='white', font=('bold',16), borderwidth=0.5)
    delButt.place(x=342, y=346, relwidth=0.05, relheight=0.05)

    butt1 = Button(newWin, text='save', command=ins,  bg='#f68c1d', fg='white', font=('bold',10), borderwidth=0.5)
    butt1.place(x=298, y=392, relwidth=0.14, relheight=0.05)

    butt4 = Button(newWin, text='+', command=openFile,  bg='#78db4d', fg='white', font=('bold',24), borderwidth=0.5)
    butt4.place(x=298, y=300, relwidth=0.14, relheight=0.05)
 
#mainWindow
main = Tk()
main.resizable(0,0)
main.geometry('228x100+276+120')
main.title('Menu')
main.iconbitmap('icon.ico')

mainButt1 = Button(main, text='Enter Word,Image to PDF Converter', command=win2)
mainButt1.place(x=13, y=20)

mainButt2 = Button(main, text='Enter Student Assignment Recorder', command=win3)
mainButt2.place(x=13, y=60, relwidth=0.875)

main.mainloop()