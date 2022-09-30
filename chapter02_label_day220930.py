from tkinter import *
from PIL import Image,ImageTk


num = 100
#倒计时100秒
def digit_count(label_count):
    def counting():
        global num
        num -=1
        label_count.config(text=str(num))
        label_count.after(300,counting)
    counting()

def test_basc_tkinter():
    root = Tk()
    #标题
    root.title('it is tkinter window')
    #背景
    root.configure(bg='#356274')
    width = 480
    height = 600
    x = (root.winfo_screenwidth()-width)//2
    y = (root.winfo_screenheight() - height)//2
    loc = '{0}x{1}+{2}+{3}'.format(width,height,x,y)
    print(loc)
    #位置及尺寸
    root.geometry(loc)

    #图标
    root.iconbitmap('./logo.ico')

    label = Label(root,width=30,height=1,
                  text='this is label',
                  fg='#13f431',bg='#545498',
                  anchor='sw',
                  font=('Helvetic',20,'bold'),
                  cursor='heart'
                  )
    label2 = Label(root,bitmap='hourglass',text='my sky is blue',compound='top',relief='solid',
                   padx=10,pady=5)

    label3 = Label(root,width=10,height=1,text='1',bg='#8712e7')
    digit_count(label3)
    label.pack()
    label2.pack()
    label3.pack()


    root.mainloop()

if __name__ == '__main__':
    test_basc_tkinter()