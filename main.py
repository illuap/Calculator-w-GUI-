from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty,StringProperty

from NumDisplay import NumDisplay

class RootWidget(Widget):

    pass

class SideMenu(Widget):
    pass

class MyApp(App):


    def build(self):
        layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(30):
            btnlol = Button(text=str(i), size_hint_y=None, height=50)
            layout.add_widget(btnlol)
        root = ScrollView(size_hint=(1, 1))
        
        root.add_widget(layout)





        num = NumDisplay()

        upperLayout = BoxLayout(orientation = 'horizontal')
        upperLayout.add_widget(num)
        upperLayout.add_widget(root)
        mainLayout = BoxLayout(orientation = 'vertical')
        mainLayout.add_widget(upperLayout)
        


        # =======================
        # === NUMBER BUTTONS  ===
        # =======================
        def callback(instance):
            print('Button <%s> is being pressed' % instance.text)
            print("number: <%s> || answer: <%s>" % (num.number,num.answer))
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
            elif instance.text == "0":
                num.addZero(1)
            elif instance.text == "00":
                num.addZero(2)

        btn1 = Button(text='1')
        btn2 = Button(text='2')
        btn3 = Button(text='3')
        btn4 = Button(text='4')
        btn5 = Button(text='5')
        btn6 = Button(text='6')
        btn7 = Button(text='7')
        btn8 = Button(text='8')
        btn9 = Button(text='9')
        btn0 = Button(text='0')
        btn00 = Button(text='00')
        btnDot= Button(text='.')


        btn1.bind(on_press=callback)
        btn2.bind(on_press=callback)
        btn3.bind(on_press=callback)
        btn4.bind(on_press=callback)
        btn5.bind(on_press=callback)
        btn6.bind(on_press=callback)
        btn7.bind(on_press=callback)
        btn8.bind(on_press=callback)
        btn9.bind(on_press=callback)
        btn0.bind(on_press=callback)
        btn00.bind(on_press=callback)
        btnDot.bind(on_press=callback)
        # ------------------------------------------------------------


        # ===================
        # === ADD BUTTON  ===
        # ===================
        def add(instance):
            print("Adding ", num.number," to ", num.answer )
            num.setOperation("+")

        btnAdd = Button(text='+', size_hint_x=None, width=150)
        btnAdd.bind(on_press=add)
        # ------------------------------------------------------------

        # ===================
        # === SUB BUTTON  ===
        # ===================
        def sub(instance):
            print("Subtracting" , num.number," from ", num.answer )
            num.setOperation("-")

        btnSub = Button(text='-', size_hint_x=None, width=150)
        btnSub.bind(on_press=sub)
        # ------------------------------------------------------------


        # ========================
        # === Multiply BUTTON  ===
        # ========================
        def mult(instance):
            print("Multiplying" )
            num.setOperation("*")

        btnMult = Button(text='*')
        btnMult.bind(on_press=mult)
        # ------------------------------------------------------------

        # ======================
        # === Divide BUTTON  ===
        # ======================
        def div(instance):
            print("DIviding" )
            num.setOperation("/")

        btnDiv = Button(text='/')
        btnDiv.bind(on_press=div)
        # ------------------------------------------------------------

        # ======================
        # === Recall BUTTON  ===
        # ======================
        def recall(instance):
            print(num.recallNumber())

        btnRecall = Button(text='Recall')
        btnRecall.bind(on_press=recall)
        # ------------------------------------------------------------

        # =========================
        # === BackSpace BUTTON  ===
        # =========================
        def bkSpace(instance):
            print("ERASING A NUMBER" )
            num.backSpace()

        btnBkS = Button(text='<-', size_hint_x=None, width=150)
        btnBkS.bind(on_press=bkSpace)
        # ------------------------------------------------------------

        # =====================
        # === ENTER BUTTON  ===
        # =====================
        def enter(instance):
            print("enter was pressed")
            num.equalNumber();
        btnEnter = Button(text='Enter', size_hint_x=None, width=150)
        btnEnter.bind(on_press=enter)
        # ------------------------------------------------------------




        # ===================
        # ===   LAYOUT    ===
        # ===================   
        buttonLayout = GridLayout(cols = 4)
        buttonLayout.add_widget(btnMult)
        buttonLayout.add_widget(btnDiv)
        buttonLayout.add_widget(btnRecall)
        buttonLayout.add_widget(btnBkS)
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
        buttonLayout.add_widget(btnEnter)
        buttonLayout.add_widget(btn0)
        buttonLayout.add_widget(btn00)
        buttonLayout.add_widget(btnDot)
        mainLayout.add_widget(buttonLayout)

        return mainLayout


if __name__ == '__main__':
    MyApp().run()
