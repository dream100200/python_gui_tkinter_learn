from tkinter import *


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


    root.mainloop()

if __name__ == '__main__':
    test_basc_tkinter()
