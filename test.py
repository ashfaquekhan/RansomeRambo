import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication,  QPlainTextEdit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import pyqtSlot
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller
import pyperclip as pc 
import os
keyboard = Controller()

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel(self)
        pixmap = QPixmap('new.png')
        label.setPixmap(pixmap)
        label.setGeometry(0,0,900,400) 
        self.title = 'COPYCAT'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ###########
        combo = QComboBox(self)
        shotcut_list = ["Key.f9","Key.f2","Key.f3","Key.f4","Key.f5","Key.f6","Key.f7","Key.f8","Key.f1","Key.f10","Key.f11","Key.f12"]
        combo.addItems(shotcut_list)
        global shortcut 
        shortcut = combo.currentText()
        combo.setGeometry(350, 120, 120, 30)
        # Create textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 160)
        self.textbox.setReadOnly(True)
        self.textbox.resize(500,205)
        combo.activated[str].connect(self.onChanged)  
        self.setGeometry(70,70,540,388)
        self.show()
 
    def onChanged(self, text):
        global shortcut
        shortcut=text

    def print_key(*key):
        if str(key[1]) == shortcut:
            cptext = pc.paste()     
            keyboard.type(cptext)

    def key(self):     
        listener = Listener(on_press=self.print_key)
        listener.start()
    

if __name__ == '__main__':
    appctxt = ApplicationContext()
    app = QApplication(sys.argv)
    ex = App()
    ex.key()
    sys.exit(appctxt.app.exec_())