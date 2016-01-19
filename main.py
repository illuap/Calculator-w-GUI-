from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty

class RootWidget(Widget):

    pass

class NumDisplay(Widget):
    number = NumericProperty(0)
    number2 = NumericProperty(0)
    def clickNum(self, x):
        self.number = self.number*10
        self.number += x
    def addNumber(self):
        self.number2 += self.number
        self.number = 0
    def subNumber(self):
        self.number2 -= self.number
        self.number = 0
    

class MyApp(App):


    def build(self):
        num = NumDisplay()

        mainLayout = BoxLayout(orientation = 'vertical')
        mainLayout.add_widget(num)
        
        def callback(instance):
            print('Button <%s> is being pressed' % instance.text)
            if instance.text == "1":
                num.clickNum(1)
            elif instance.text == "2":
                num.clickNum(2)
            elif instance.text == "3":
                num.clickNum(3)
            elif instance.text == "4":
                num.clickNum(4)
            elif instance.text == "5":
                num.clickNum(5)
            elif instance.text == "6":
                num.clickNum(6)
            elif instance.text == "7":
                num.clickNum(7)
            elif instance.text == "8":
                num.clickNum(8)
            elif instance.text == "9":
                num.clickNum(9)

        btn1 = Button(text='1')
        btn2 = Button(text='2')
        btn3 = Button(text='3')
        btn4 = Button(text='4')
        btn5 = Button(text='5')
        btn6 = Button(text='6')
        btn7 = Button(text='7')
        btn8 = Button(text='8')
        btn9 = Button(text='9')



        btn1.bind(on_press=callback)
        btn2.bind(on_press=callback)
        btn3.bind(on_press=callback)
        btn4.bind(on_press=callback)
        btn5.bind(on_press=callback)
        btn6.bind(on_press=callback)
        btn7.bind(on_press=callback)
        btn8.bind(on_press=callback)
        btn9.bind(on_press=callback)


        def add(instance):
            print("Adding ", num.number," to ", num.number2 )
            num.addNumber()

        btnAdd = Button(text='+', size_hint_x=None, width=150)
        btnAdd.bind(on_press=add)


        def sub(instance):
            print("Subtracting" , num.number," from ", num.number2 )
            num.subNumber()

        btnSub = Button(text='-', size_hint_x=None, width=150)
        btnSub.bind(on_press=sub)


        buttonLayout = GridLayout(cols = 4)
        buttonLayout.add_widget(btn1)
        buttonLayout.add_widget(btn2)
        buttonLayout.add_widget(btn3)
        buttonLayout.add_widget(btnAdd)
        buttonLayout.add_widget(btn4)
        buttonLayout.add_widget(btn5)
        buttonLayout.add_widget(btn6)
        buttonLayout.add_widget(btnSub)
        buttonLayout.add_widget(btn7)
        buttonLayout.add_widget(btn8)
        buttonLayout.add_widget(btn9)
        buttonLayout.add_widget(Button(text='Enter', size_hint_x=None, width=150))
        
        mainLayout.add_widget(buttonLayout)

        return mainLayout


if __name__ == '__main__':
    MyApp().run()
