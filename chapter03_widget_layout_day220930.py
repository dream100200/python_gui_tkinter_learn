from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Separator



def test_layout_widget():
    window = Tk()
    window.title('this is layout test')

    #背景
    window.configure(bg='#356274')
    width = 480
    height = 600
    x = (window.winfo_screenwidth()-width)//2
    y = (window.winfo_screenheight() - height)//2
    loc = '{0}x{1}+{2}+{3}'.format(width,height,x,y)
    print(loc)
    #位置及尺寸
    window.geometry(loc)

    label01 = Label(window,text='国庆节快乐',width=15,bg='#E12111')
    label02 = Label(window, text='中秋节快乐', width=15, bg='#812111')
    label03 = Label(window, text='三八节快乐', width=15, bg='#319111')

    label01.pack(side=LEFT) #LEFT RIGHT BOTTOM TOP
    label02.pack(side=LEFT)
    label03.pack(side=LEFT)

    window.mainloop()

if __name__ == '__main__':
    test_layout_widget()