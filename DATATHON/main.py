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
Window.size = (500, 600)

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
    temp: chk_temp
    humid: chk_humid
    dust: chk_dust
    co2: chk_co2
    
    Image:
        source: "pictures/page2.png"

    GridLayout: 
        cols: 4
        padding : 1,1
        spacing: 1
        row_default_height: '10dp'

        Label:
            text: 'temp'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id : chk_temp
            width: 10

        Label:
            text: 'humid'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id: chk_humid
            width: 10
            
        Label:
            text: 'dust'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id: chk_dust
            width: 10
            
        Label:
            text: 'co2'
            text_size: self.size
            valign: 'middle'
            width: 10

        CheckBox:
            group: 'check'
            id: chk_co2
            width: 10
        
        Label:
            text: 'warm'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id: chk_warm
            width: 10

            
        Label:
            text: 'cold'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id: chk_cold
            width: 10
          

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
            source: "pictures/2nd.png"
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
    temp = ObjectProperty(None)
    humid = ObjectProperty(None)
    dust = ObjectProperty(None)
    co2 = ObjectProperty(None)
    warm = ObjectProperty(None)
    cold = ObjectProperty(None)

    def insert_data(self):
        if self.temp.active:
            print('temp')
        elif self.humid.active:
            print('humid')
        elif self.dust.active:
            print('dust')
        else:
            print('co2')

    def insert_data2(self):
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
        im2 = Image(source="pictures/2nd.png")
        layout2.add_widget(im2)

        self.add_widget(layout1)
        self.add_widget(layout2)


screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))


class ScreenApp(App):
    def build(self):
        return screen_manager


sample_app = ScreenApp()
sample_app.run()
