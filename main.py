from functools import partial
import random
from tkinter import W, messagebox
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)

        self.game = [[None for i in range (9)] for j in range (9)]

        for i in range (9):
            for j in range (9):
                linedit = QLineEdit()
                linedit.setStyleSheet('font-size: 28px')
                linedit.setSizePolicy(QSizePolicy.Preferred , QSizePolicy.Preferred)
                self.game[i][j] = linedit
                self.ui.grid_layout.addWidget(linedit ,i ,j)
                self.game[i][j].setAlignment(Qt.AlignCenter)
                linedit.textChanged.connect(self.check_func)

        self.ui.show()
        self.flag = 0
        
        for i in range(9):
            for j in range(9):
                self.game[i][j].setEnabled(False)
        
        self.ui.New_Button.clicked.connect(self.newgame_func)
        self.ui.check_button.clicked.connect(self.check_func)
        self.ui.restart_button.clicked.connect(self.restart_func)
        self.ui.mode_button.clicked.connect(self.change_mod)
    
    def newgame_func(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setEnabled(True)
        
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')
        
        x = random.randint(1,6)
        file = open(f"s{x}.txt" , 'r')
        row_numbers = file.read().split('\n')
        #row_numbers = numbers        
        for i in range(9):
            num = row_numbers[i].split(' ')
            for j in range(9):
                if num[j] != '0' and num[j] != '' :
                    if self.flag == 1 :
                        self.game[i][j].setStyleSheet('font-size: 28px; color: white')
                        self.game[i][j].setText(num[j])
                    else:
                        self.game[i][j].setStyleSheet('font-size: 28px; color: Black')
                        self.game[i][j].setText(num[j])
                    self.game[i][j].setEnabled(False)
                else:
                    self.game[i][j].setStyleSheet('font-size: 28px; color: green')
    
    def restart_func(self):
        
        for i in range(9):
            for j in range(9):
                if self.game[i][j].setEnabled(True):
                    self.game[i][j].setText('')
                    self.game[i][j].setStyleSheet('font-size: 28px; color: green')
                else:
                    if self.flag == 0 :
                        self.game[i][j].setStyleSheet('font-size: 28px; color: Black')
                    else:
                        self.game[i][j].setStyleSheet('font-size: 28px; color: white')     

    def change_mod(self):
        self.flag = 1
        self.ui.setStyleSheet('background-color: black')
        for i in range (9):
            for j in range (9):
                self.game[i][j].setStyleSheet('font-size: 28px; color: white; background-color: black')

        self.ui.New_Button.setStyleSheet('color: white; background-color: darkgray')
        self.ui.check_button.setStyleSheet('color: white; background-color: darkgray')
        self.ui.restart_button.setStyleSheet('color: white; background-color: darkgray')
        self.ui.mode_button.setStyleSheet('color: white; background-color: darkgray')
    

    def check_func(self):
        self.win = True

        #check rows 9*9
        for row in range(9):
            for i in range(9):
                for j in range(i+1 ,9):
                    if self.game[row][i].text() == self.game[row][j].text() and self.game[row][i].text() != '':
                        self.game[row][i].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                        self.game[row][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                        self.win = False
        
        #check columns 9*9
        for col in range(9):
            for i in range(9):
                for j in range(i+1 ,9):
                    if self.game[i][col].text() == self.game[j][col].text() and self.game[i][col].text() != '':
                        self.game[i][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                        self.game[j][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                        self.win = False
        #3*3 
        for row in range(3):
            for col in range(3):
                for i in range(3):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
 
        for row in range(3):
            for col in range(3,6):
                for i in range(3):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False

        for row in range(3):
            for col in range(6,9):
                for i in range(3):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False        
        
        for row in range(3,6):
            for col in range(3):
                for i in range(3,6):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
        
        for row in range(3,6):
            for col in range(3,6):
                for i in range(3,6):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
        
        for row in range(3,6):
            for col in range(6,9):
                for i in range(3,6):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
        
        for row in range(6,9):
            for col in range(3):
                for i in range(6,9):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
        
        for row in range(6,9):
            for col in range(3,6):
                for i in range(6,9):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
        
        for row in range(6,9):
            for col in range(6,9):
                for i in range(6,9):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and i!=row and j!=col and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.game[i][j].setStyleSheet('font-size: 28px; color: black; background-color: pink')
                            self.win = False
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    self.win = False
        
        if self.win == True:
            box = QMessageBox()
            box.setText(' YOU WON! ')
            box.exec()

app = QApplication([])
window = MainWindow()
app.exec()