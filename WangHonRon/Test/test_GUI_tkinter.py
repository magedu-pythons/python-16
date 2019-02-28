from tkinter import *

class mygui:
    def __init__(self):

        self.root = Tk(className='登录') #初始化窗口
        #lbl = Label(self.root)
        #lbl['text'] = '姓名：'
        #lbl.pack()
        self.root['background'] = 'white'
        self.root['height'] = 400
        self.root['width'] = 600
        self.root['cursor'] = 'coffee_mug'
        self.root.title('测试GUI程序')
        self.root.resizable(False,False)


        self.root = mainloop()



if __name__ == '__main__':
    myGUI = mygui()
