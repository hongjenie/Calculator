from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5 import uic

import sys
import math 

# 'Test.ui' 파일에서 위젯 클래스를 로드합니다.
from_class = uic.loadUiType("Calculator.ui")[0]

class WindowClass(QMainWindow, from_class) :

    def __init__(self):
        super().__init__()
        self.setupUi(self)
 
        # setting title
        self.setWindowTitle("Calculator")

        self.minus.clicked.connect(self.action_minus)
        self.equal.clicked.connect(self.action_equal)
        self.pushButton_0.clicked.connect(lambda : self.action("0"))
        self.pushButton_1.clicked.connect(lambda : self.action("1"))
        self.pushButton_2.clicked.connect(lambda : self.action("2"))
        self.pushButton_3.clicked.connect(lambda : self.action("3"))
        self.pushButton_4.clicked.connect(lambda : self.action("4"))
        self.pushButton_5.clicked.connect(lambda : self.action("5"))
        self.pushButton_6.clicked.connect(lambda : self.action("6"))
        self.pushButton_7.clicked.connect(lambda : self.action("7"))
        self.pushButton_8.clicked.connect(lambda : self.action("8"))
        self.pushButton_9.clicked.connect(lambda : self.action("9"))
        self.divide.clicked.connect(self.action_div)
        self.multiple.clicked.connect(self.action_mul)
        self.plus.clicked.connect(self.action_plus)
        self.point.clicked.connect(self.action_point)                    
        self.AC.clicked.connect(self.action_clear)                           
        self.pushButton_Delete.clicked.connect(self.action_del)
        self.Sqrt.clicked.connect(self.action_sqrt)
        self.pow_button.clicked.connect(self.action_pow)
        self.Factorial.clicked.connect(self.action_factorial)
        self.PI.clicked.connect(self.PI_action)

        # showing all the widgets
        self.show()
        
        # number to 0
        self.number = 0
        self.previous_number = None

    def action_equal(self):
        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            answer = eval(equation)
 
            # setting text to the label
            self.label.setText(str(answer))
 
        except:
            # setting text to the label
            self.label.setText("Wrong Input. Try again.")

    def action_close(self):
        text = self.label.text()
        self.label.setText(text + ")")    

    # plus, minus, mul, div 

    def action_plus(self):
        # appending label text
        text = self.label.text()

        # check digit and prevent from "+" entering more than once
        # if절안에 text가 null이 아니면 text[:-1]가 숫자가 아니라면이라는 뜻 
        
        if text and not text[-1].isdigit() and (text[-1] == text['(' or ')']):        
            text = text[:-1]  
        else:
            self.label.setText(text + "+")    

    def action_minus(self):
        # appending label text
        text = self.label.text()
        
        # check digit and prevent from "-" entering more than once
        
        if text and not text[-1].isdigit():        
            text = text[:-1]
        
        else:
            self.label.setText(text + "-")    

    def action_div(self):
        # appending label text
        text = self.label.text()

        # check digit and prevent from "/" entering more than once

        if text and not text[-1].isdigit():        
            text = text[:-1]
        else:
            self.label.setText(text + "/")    

    def action_mul(self):
        # appending label text
        text = self.label.text()
        
        # check digit and prevent from "*" entering more than once

        if text and not text[-1].isdigit():        
            text = text[:-1]
        else:
            self.label.setText(text + "*")    

    def action_point(self):
        # appending label text
        text = self.label.text()

        # check digit and prevent from "*" entering more than once

        # if절안에 text가 null이 아니면 이라는 뜻에서 if text and not 이라는 의미가 있는것이다 
        if text and not text[-1].isdigit():     
            text = text[:-1]
        else:
            self.label.setText(text + ".")    

    # sqrt, factorial, pow

    def action_sqrt(self):
        try:        
            text = self.label.text()
            input_number = float(text)

            if input_number < 0:
                self.label.setText("INPUT POSITIVE NUMBER")
                                
            else:
                sqrt_number = math.sqrt(input_number)
                self.label.setText(str(sqrt_number))
        except ValueError:
            self.label.setText("INVALID NUMBER")
            text = self.label.text()            

    def action_factorial(self):
        try: 
            # 입력된 텍스트를 정수로 변환
            text = self.label.text()
            input_number = int(text)

            if input_number < 0:
                self.label.setText("INPUT POSITIVE NUMBER")

            else:
                # 팩토리얼 계산
                factorial_number = math.factorial(input_number)
                # 계산 결과를 Label에 표시
                self.label.setText(str(factorial_number))

        except ValueError:
            self.label.setText("WRONG or OVER NUMBER. INVALID INPUT")
            text = self.label.text()                            

    def action_pow(self):
        try: 
            text = self.label.text()
            input_number = float(text)

            if input_number < 0:
                self.label.setText("INVALID NUMBER")
           
            else:
                pow_number = math.pow(input_number, 2)
                self.label.setText(str(pow_number))

        except ValueError:
            self.label.setText("WRONG or OVER NUMBER. INVALID INPUT")
            text = self.label.text()

    # number button 

    def action(self, text):
        current_text = self.label.text()
        new_text = current_text + text
        self.label.setText(new_text)    

    # action clear, del, PI, open, close

    def action_clear(self):
        # clearing the label text
        self.label.setText("")
 
    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1]) and self.label.setText(text[len(text)+2])
    
    def PI_action(self):
        PI_number = round(math.pi, 6)
        text = self.label.text()
        self.label.setText(text + str(PI_number)) 
    
    # def action_open(self):
    #     text = self.label.text()
    #     self.label.setText(text + "(")
    
    # def action_close(self):
    #     text = self.label.text()
    #     self.label.setText(text + ")")          

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())















