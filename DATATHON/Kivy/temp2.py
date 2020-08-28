import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

kivy.require('1.11.1')

Builder.load_string(""" 
#:import Clock kivy.clock.Clock
<ScreenOne>: 
    BoxLayout: 
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page1.png"
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_release: 
                Clock.schedule_once(root.callbackfun, 4)
            on_press: root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_two'

<CustomLabel@Label>:
    text_size: self.size
    valign: "middle"
    padding_x: 1

<GreenButton@Button>:
    background_color: 1, 1, 1, 1
    size_hint_y: None
    height: self.parent.height * 0.120

<ScreenTwo>: 
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
    RelativeLayout:
        Button:
            id: button1
            text: 'One'
            size_hint: (.01, .01)
            pos: (150, 505)
            on_press: root.callback()
        Button:
            id: button2
            text: "pos_hint "
            background_color: 0.1, 0.5, 0.6, 1
            size_hint: (.1, .1)
            pos_hint: {"x":0, "top":1}
            on_press: root.callback()
        Button:
            id: button3
            text: 'Three'
            size_hint: (.1, .1)
            pos: (150, 50)
            on_press: root.callback()
        Button:
            id: button4
            text: 'Four'
            size: (32, 32)
            size_hint: (.1, .1)
            pos: (100, 50)
            on_press: root.callback()

    BoxLayout: 
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: 
                root.insert_data()
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_three' 


<ScreenThree>: 
    BoxLayout: 
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page3.png"
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_four' 


<ScreenFour>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4.png"
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/FB1.png"
            pos_hint: {'left': 1, 'top': 3}
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_five'

<ScreenFive>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4.png"
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/F1.png"
            pos_hint: {'left': 1, 'top': 3}
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_six'
<ScreenSix>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4.png"
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/F2.png"
            pos_hint: {'left': 1, 'top': 3}
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_seven'
<ScreenSeven>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4.png"
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/F3.png"
            pos_hint: {'left': 1, 'top': 3}
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_eight'
<ScreenEight>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4.png"
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/F4.png"
            pos_hint: {'left': 1, 'top': 3}
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_nine'
<ScreenNine>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4.png"
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/F5.png"
            pos_hint: {'left': 1, 'top': 3}      
        Button:
            text: 'Close'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: app.stop()
""")


class ScreenOne(Screen):
    def on_enter(self, *args):
        print("on Enter")
        if self.manager.current != "pictures/page2.png":
            Clock.schedule_once(self.callbackfun, 4)

    def callbackfun(self, dt):
        print("Change Screen")
        print(self.manager.current)
        print(self.manager.next())
        self.manager.current = self.manager.next()


class ScreenTwo(Screen):
    warm = ObjectProperty(None)
    cold = ObjectProperty(None)

    def callback(self):
        print('The button <%s> is being pressed')

    btn1 = Button(text='Hello world 1')
    btn1.bind(on_press=callback)
    btn2 = Button(text='Hello world 2')
    btn2.bind(on_press=callback)

    def insert_data(self):
        if self.warm.active:
            print('warm')
        else:
            print('cold')


class ScreenThree(Screen):
    pass


class ScreenFour(Screen):
    def __init__(self, **kwargs):
        super(ScreenFour, self).__init__(**kwargs)
        self.size = Window.size

        layout1 = BoxLayout()
        im1 = Image(source="pictures/page4.png")
        layout1.add_widget(im1)

        layout2 = BoxLayout()
        im2 = Image(source="pictures/FB1.png")
        layout2.add_widget(im2)

        self.add_widget(layout1)
        self.add_widget(layout2)


class ScreenFive(Screen):
    def __init__(self, **kwargs):
        super(ScreenFive, self).__init__(**kwargs)
        self.size = Window.size

        layout3 = BoxLayout()
        im3 = Image(source="pictures/page4.png")
        layout3.add_widget(im3)

        layout4 = BoxLayout()
        im4 = Image(source="pictures/F1.png")
        layout4.add_widget(im4)

        self.add_widget(layout3)
        self.add_widget(layout4)


class ScreenSix(Screen):
    def __init__(self, **kwargs):
        super(ScreenSix, self).__init__(**kwargs)
        self.size = Window.size

        layout5 = BoxLayout()
        im5 = Image(source="pictures/page4.png")
        layout5.add_widget(im5)

        layout6 = BoxLayout()
        im6 = Image(source="pictures/F2.png")
        layout6.add_widget(im6)

        self.add_widget(layout5)
        self.add_widget(layout6)


class ScreenSeven(Screen):
    def __init__(self, **kwargs):
        super(ScreenSeven, self).__init__(**kwargs)
        self.size = Window.size

        layout7 = BoxLayout()
        im7 = Image(source="pictures/page4.png")
        layout7.add_widget(im7)

        layout8 = BoxLayout()
        im8 = Image(source="pictures/F3.png")
        layout8.add_widget(im8)

        self.add_widget(layout7)
        self.add_widget(layout8)


class ScreenEight(Screen):
    def __init__(self, **kwargs):
        super(ScreenEight, self).__init__(**kwargs)
        self.size = Window.size

        layout9 = BoxLayout()
        im9 = Image(source="pictures/page4.png")
        layout9.add_widget(im9)

        layout10 = BoxLayout()
        im10 = Image(source="pictures/F4.png")
        layout10.add_widget(im10)

        self.add_widget(layout9)
        self.add_widget(layout10)


class ScreenNine(Screen):
    def __init__(self, **kwargs):
        super(ScreenNine, self).__init__(**kwargs)
        self.size = Window.size

        layout11 = BoxLayout()
        im11 = Image(source="pictures/page4.png")
        layout11.add_widget(im11)

        layout12 = BoxLayout()
        im12 = Image(source="pictures/F5.png")
        layout12.add_widget(im12)

        self.add_widget(layout11)
        self.add_widget(layout12)


screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))
screen_manager.add_widget(ScreenFive(name="screen_five"))
screen_manager.add_widget(ScreenSix(name="screen_six"))
screen_manager.add_widget(ScreenSeven(name="screen_seven"))
screen_manager.add_widget(ScreenEight(name="screen_eight"))
screen_manager.add_widget(ScreenNine(name="screen_nine"))


class ScreenApp(App):
    def build(self):
        return screen_manager


sample_app = ScreenApp()
sample_app.run()
