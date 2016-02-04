from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty,StringProperty
import math

class NumDisplay(Widget):
    number = NumericProperty(0)
    answer = NumericProperty(0)
    operation = NumericProperty(0)
    equation = StringProperty("")
    equation2 = StringProperty("")
    answer2 = NumericProperty(0)
    digits = NumericProperty(0)
    def clickNum(self, x):
        self.number = self.number*10
        self.number += x
        self.digits += 1
        self.equation += str(x)
        print (self.digits)
        
        
    def addNumber(self):
        self.doOperation(self.checkOperation())
        self.changeSign("+")
    def subNumber(self):
        self.doOperation(self.checkOperation())
        self.changeSign("-")
    def equalNumber(self):
        self.doOperation(self.checkOperation())
        self.changeSign(" =")
        self.answer2 = self.answer
        self.equation2 = self.equation +" "+ str(self.answer)
        self.equation = ""

    #number turns to 0 
            #therefore digits in number is 0

    def doOperation(self,x):
        if(x == "+"):
            self.answer += self.number
            self.number = 0
            self.digits = 0 
        elif(x == "-"):
            self.answer -= self.number
            self.number = 0
            self.digits = 0
        ##SUBSTITUDE
        elif(x == "x"):
            self.answer *= self.number
            self.number = 0
            self.digits = 0
        elif(x == "/"):
            self.answer /= self.number
            self.number = 0
            self.digits = 0
        #if there is no sign (the start)
        else:
            self.answer = self.number
            self.number = 0
            self.digits = 0
    def checkSign(self):
        try:
            if(ord(self.equation[-1]) < ord('0')  or  ord(self.equation[-1]) > ord('9')):
                return False
            else:
                return True
        except:
            return True

    def changeSign(self,sign):
        if(self.checkSign()):
            self.equation += sign
        else:
            self.equation = self.equation[:-1]
            self.equation += sign

    def checkOperation(self):
        try:
            print(self.equation[-(self.digits+1)])
            return self.equation[-(self.digits+1)]
        except:
            return None
    

    def updateEquation(self,type,x):
        self.equation = self.equation[:-1]
        self.equation += type + " "+ str(x) + " " 
        self.equation += "="

    def recallAnswer(self):
        for x in str(self.answer2):
                self.digits += 1
        self.number = int(self.number*math.pow(10,self.digits))
        self.number += self.answer2
        self.equation += str(self.answer2)
        return self.answer2