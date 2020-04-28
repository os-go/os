from tkinter import *
import tkinter.filedialog

def xz():
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='完整路径：'+filename+'\n已拷贝至剪贴板')
         import pyperclip as p1
         p1.copy(filename)
         stam = p1.paste()
         
    else:
         lb.config(text='您没有选择任何文件，无法查询')

root = Tk()
root.geometry('600x600')
lb = Label(root,text='')
lb.pack()
btn=Button(root,text='选择文件并查询',command=xz)
btn.pack()
root.mainloop()