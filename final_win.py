from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont 
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.show()
        
        def results(self):
            if self.exp.age < 7:
                self.index = 0
            return "нет данных для такого возраста"
            self.index = (4 * (int(self.exp.t1)+int(self.exp.t2)))
        if self.exp.age == 7 or self.exp.age == 8 :
            if self.index >=21:
                return txt_res1
            elif self.index <21 and self.index >= 17:
                 return txt_res2
            elif self.index <17 and self.index >=12:
                return txt_res3
            elif self.index <12 and self.index >=6.5:
                return txt_res4
            else:
                return txt_res5
            if self.exp.age == 9 and self.exp.age == 10:  
                if self.index >=19.5:
                    return txt_res1
                elif self.index < 19.5 and self.index >= 15.5:
                    return txt_res2
                                         
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = Label(text_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self. move(win_x, win_y)

app = QApplication([])
mw = FinalWin()
app.exec_()
