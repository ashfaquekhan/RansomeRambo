import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,  QPlainTextEdit, QApplication, QMainWindow, QLabel, QComboBox
from PyQt5.QtGui import QPixmap
from pynput import keyboard
from pynput.keyboard import Listener, Controller
import pyperclip as pc 

keyboard = Controller()
class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        #super().__init__()
        label = QLabel(self)
        pixmap = QPixmap('E:/copycat/new.png')
        label.setPixmap(pixmap)
        label.setGeometry(0,0,900,400) 
        self.title = 'COPYCAT'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
        self.key()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ###########
        combo = QComboBox(self)
        shotcut_list = [
            "Key.f9",
            "Key.f2",
            "Key.f3",
            "Key.f4",
            "Key.f5",
            "Key.f6",
            "Key.f7",
            "Key.f8",
            "Key.f1",
            "Key.f10",
            "Key.f11",
            "Key.f12",
        ]
        combo.addItems(shotcut_list)
        global shortcut
        global cptext
        shortcut = combo.currentText()
        combo.setGeometry(350, 120, 120, 30)
        combo.activated[str].connect(self.onChanged)  
        # Create textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 160)
        self.textbox.setReadOnly(True)
        self.textbox.resize(500,205)
        self.setGeometry(70,70,540,388)
        self.show()

    def onChanged(self, text):
        global shortcut
        shortcut=text
        
    def print_key(self,key):
        if str(key) == shortcut:
            cptext = pc.paste() 
            keyboard.type(cptext)
            self.textbox.insertPlainText(cptext)
            self.textbox.insertPlainText("\n")

    def key(self):    
        listener = Listener(on_press=self.print_key)
        listener.start()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    #ex.key()
    sys.exit(app.exec_())


                         