from PyQt5.QtWidgets import QWidget,QPushButton,QTextEdit,QApplication

class MyWidget(QWidget):
    def __init__(self):
        self.setGeometry(100,100,400,400)
        self.button = QPushButton(parent=self, text='确 定')
        self.button.setGeometry(100,100,100,35)
        self.show()

# 构建Qt应用程序
app = QApplication([])
# 实例一个小窗口并设置位置和大小
widget = QWidget()
widget.setGeometry(100,100,400,380)
# 实例几个控件，显示在小窗口上
txt1 = QTextEdit(parent = widget)
btn1 = QPushButton(parent = widget, text = '确 定')
btn2 = QPushButton(parent = widget, text = '取 消')
# 定义控件位置和大小
txt1.setGeometry(10,10,380,320)
btn1.setGeometry(135,335,100,35)
btn2.setGeometry(250,335,100,35)
# 显示小窗口
widget.show()
# 运行Qt应用程序
app.exec()

