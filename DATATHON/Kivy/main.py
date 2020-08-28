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
Window.size = (370, 600)
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
    BoxLayout:
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


<ScreenTwo>: 
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: "pictures/page2.png"
    RelativeLayout:
        Button:
            id: temp
            background_normal: 'pictures/button1.png'
            background_down: 'pictures/button2.png'
            size_hint: (0.04,0.02)
            pos: (36, 391)
            on_press: 
                root.temp()
                root.newtemp()    
    RelativeLayout:
        Button:
            id: humid
            background_normal: 'pictures/button1.png'
            background_down: 'pictures/button2.png'
            size_hint: (0.04,0.02)
            pos: (114, 391)
            on_press: 
                root.humid()
                root.newhumid()
    RelativeLayout:
        Button:
            id: dust
            background_normal: 'pictures/button1.png'
            background_down: 'pictures/button2.png'
            size_hint: (0.04,0.02)
            pos: (196, 391)
            on_press: 
                root.dust()
                root.newdust()
    RelativeLayout:
        Button:
            id: co2
            background_normal: 'pictures/button1.png'
            background_down: 'pictures/button2.png'
            size: (32, 32)
            size_hint: (0.04,0.02)
            pos: (277, 391)
            on_press: 
                root.co2()
                root.newco2()
    RelativeLayout:
        Button:
            id: warm
            background_normal: 'pictures/button1.png'
            background_down: 'pictures/button2.png'
            size: (32, 32)
            size_hint: (0.04,0.02)
            pos: (36, 218)
            on_press: 
                root.warm()
                root.newwarm()
                
        Button:
            id: cold
            background_normal: 'pictures/button1.png'
            background_down: 'pictures/button2.png'
            size: (32, 32)
            size_hint: (0.04,0.02)
            pos: (36, 165)
            on_press: 
                root.cold()
                root.newcold()

    BoxLayout: 
        Button:
            text: 'Next'
            size_hint: None, None
            pos_hint: {'right': 5}
            size: 80, 30
            on_press: 
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
            
    RelativeLayout:
        Button:
            id: floorB1
            background_normal: 'pictures/button_b1.png'
            size_hint: (0.19,0.11)
            pos: (147, 423)
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_four' 
                
    RelativeLayout:
        Button:
            id: floor1
            background_normal: 'pictures/button_1.png'
            size_hint: (0.19,0.11)
            pos: (242, 376)
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_five' 
            
    RelativeLayout:
        Button:
            id: floor2
            background_normal: 'pictures/button_2.png'
            size_hint: (0.19,0.11)
            pos: (243, 282)
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_six' 
                
    RelativeLayout:
        Button:
            id: floor3
            background_normal: 'pictures/button_3.png'
            size_hint: (0.19,0.11)
            pos: (147, 235)
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_seven' 
                
    RelativeLayout:
        Button:
            id: floor4
            background_normal: 'pictures/button_4.png'
            size_hint: (0.19,0.11)
            pos: (54, 282)
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_eight' 
                
    RelativeLayout:
        Button:
            id: floor5
            background_normal: 'pictures/button_5.png'
            size_hint: (0.19,0.11)
            pos: (54, 376)
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_nine' 
                



<ScreenFour>: 

    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4-b1.png"
    RelativeLayout:
        Button:
            id:bf1bf1
            text: 'B1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 0, 1)
            size_hint:(0.123,0.055)
            pos: (30,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_four'      
    RelativeLayout:
        Button:
            id:bf1f1
            text: 'F1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (83,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_five'
    RelativeLayout:
      
        Button:
            id:bf1f2
            text: 'F2'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (136,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_six'
    RelativeLayout:
    
        Button:
            id:bf1f3
            text: 'F3'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (186,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_seven'
    RelativeLayout:
        
        Button:
            id:bf1f4
            text: 'F4'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (238,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_eight'
                
    RelativeLayout:
        
        Button:
            id:bf1f5
            text: 'F5'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (293,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_nine'      
        

<ScreenFive>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4-1.png"
    RelativeLayout:
        Button:
            id:bf1bf1
            text: 'B1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (30,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_four'      
    RelativeLayout:
        Button:
            id:bf1f1
            text: 'F1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 0, 1)
            size_hint:(0.123,0.055)
            pos: (83,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_five'
    RelativeLayout:
      
        Button:
            id:bf1f2
            text: 'F2'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (136,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_six'
    RelativeLayout:
    
        Button:
            id:bf1f3
            text: 'F3'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (186,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_seven'
    RelativeLayout:
        
        Button:
            id:bf1f4
            text: 'F4'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (238,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_eight'
                
    RelativeLayout:
        
        Button:
            id:bf1f5
            text: 'F5'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (293,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_nine'    
                
<ScreenSix>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4-2.png"
    RelativeLayout:
        Button:
            id:bf1bf1
            text: 'B1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (30,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_four'      
    RelativeLayout:
        Button:
            id:bf1f1
            text: 'F1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (83,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_five'
    RelativeLayout:
      
        Button:
            id:bf1f2
            text: 'F2'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 0, 1)
            size_hint:(0.123,0.055)
            pos: (136,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_six'
    RelativeLayout:
    
        Button:
            id:bf1f3
            text: 'F3'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (186,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_seven'
    RelativeLayout:
        
        Button:
            id:bf1f4
            text: 'F4'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (238,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_eight'
                
    RelativeLayout:
        
        Button:
            id:bf1f5
            text: 'F5'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (293,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_nine'    
<ScreenSeven>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4-3.png"
    RelativeLayout:
        Button:
            id:bf1bf1
            text: 'B1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (30,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_four'      
    RelativeLayout:
        Button:
            id:bf1f1
            text: 'F1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (83,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_five'
    RelativeLayout:
      
        Button:
            id:bf1f2
            text: 'F2'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (136,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_six'
    RelativeLayout:
    
        Button:
            id:bf1f3
            text: 'F3'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 0, 1)
            size_hint:(0.123,0.055)
            pos: (186,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_seven'
    RelativeLayout:
        
        Button:
            id:bf1f4
            text: 'F4'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (238,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_eight'
                
    RelativeLayout:
        
        Button:
            id:bf1f5
            text: 'F5'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (293,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_nine'    
<ScreenEight>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4-4.png"
    RelativeLayout:
        Button:
            id:bf1bf1
            text: 'B1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (30,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_four'      
    RelativeLayout:
        Button:
            id:bf1f1
            text: 'F1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (83,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_five'
    RelativeLayout:
      
        Button:
            id:bf1f2
            text: 'F2'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (136,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_six'
    RelativeLayout:
    
        Button:
            id:bf1f3
            text: 'F3'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (186,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_seven'
    RelativeLayout:
        
        Button:
            id:bf1f4
            text: 'F4'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 0, 1)
            size_hint:(0.123,0.055)
            pos: (238,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_eight'
                
    RelativeLayout:
        
        Button:
            id:bf1f5
            text: 'F5'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (293,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_nine'    
<ScreenNine>: 
    BoxLayout:
        canvas:
            Rectangle: 
                pos: self.pos 
                size: self.size 
        Image:
            source: "pictures/page4-5.png"
    RelativeLayout:
        Button:
            id:bf1bf1
            text: 'B1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (30,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_four'      
    RelativeLayout:
        Button:
            id:bf1f1
            text: 'F1'
            color: (0, 0, 0, 1)
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (83,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_five'
    RelativeLayout:
      
        Button:
            id:bf1f2
            text: 'F2'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (136,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_six'
    RelativeLayout:
    
        Button:
            id:bf1f3
            text: 'F3'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (186,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_seven'
    RelativeLayout:
        
        Button:
            id:bf1f4
            text: 'F4'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 255, 1)
            size_hint:(0.123,0.055)
            pos: (238,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_eight'
                
    RelativeLayout:
        
        Button:
            id:bf1f5
            text: 'F5'
            color: (0, 0, 0, 1)
        
            background_color: (255, 255, 0, 1)
            size_hint:(0.123,0.055)
            pos: (293,539)
            on_press:
                root.manager.transition.direction='left'
                root.manager.transition.duration=1
                root.manager.current='screen_nine'      
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
    def temp(self, **kwargs):
        print('temp')

    def humid(self, **kwargs):
        print('humid')

    def dust(self, **kwargs):
        print('dust')

    def co2(self, **kwargs):
        print('co2')

    def warm(self, **kwargs):
        print('warm')

    def cold(self, **kwargs):
        print('cold')

    def newtemp(self):
        self.ids['temp'].background_normal = "pictures/button2.png"

    def newhumid(self):
        self.ids['humid'].background_normal = "pictures/button2.png"

    def newco2(self):
        self.ids['co2'].background_normal = "pictures/button2.png"

    def newdust(self):
        self.ids['dust'].background_normal = "pictures/button2.png"

    def newwarm(self):
        self.ids['warm'].background_normal = "pictures/button2.png"

    def newcold(self):
        self.ids['cold'].background_normal = "pictures/button2.png"


class ScreenThree(Screen):
    pass


class ScreenFour(Screen):
    def __init__(self, **kwargs):
        super(ScreenFour, self).__init__(**kwargs)
        self.size = Window.size

        layout1 = BoxLayout()
        self.im1 = Image(source="pictures/FB1.png")
        self.im1.allow_stretch = True
        self.im1.keep_ratio = False
        self.im1.size_hint_x = 0.5
        self.im1.size_hint_y = 0.3
        self.im1.pos = (50, 100)
        layout1.add_widget(self.im1)

        self.add_widget(layout1)


class ScreenFive(Screen):
    def __init__(self, **kwargs):
        super(ScreenFive, self).__init__(**kwargs)
        self.size = Window.size

        layout4 = BoxLayout()
        im4 = Image(source="pictures/F1.png")
        layout4.add_widget(im4)

        self.add_widget(layout4)


class ScreenSix(Screen):
    def __init__(self, **kwargs):
        super(ScreenSix, self).__init__(**kwargs)
        self.size = Window.size

        layout6 = BoxLayout()
        im6 = Image(source="pictures/F2.png")
        layout6.add_widget(im6)

        self.add_widget(layout6)


class ScreenSeven(Screen):
    def __init__(self, **kwargs):
        super(ScreenSeven, self).__init__(**kwargs)
        self.size = Window.size

        layout8 = BoxLayout()
        im8 = Image(source="pictures/F3.png")
        layout8.add_widget(im8)

        self.add_widget(layout8)


class ScreenEight(Screen):
    def __init__(self, **kwargs):
        super(ScreenEight, self).__init__(**kwargs)
        self.size = Window.size

        layout10 = BoxLayout()
        im10 = Image(source="pictures/F4.png")
        layout10.add_widget(im10)

        self.add_widget(layout10)


class ScreenNine(Screen):
    def __init__(self, **kwargs):
        super(ScreenNine, self).__init__(**kwargs)
        self.size = Window.size

        layout12 = BoxLayout()
        im12 = Image(source="pictures/F5.png")
        layout12.add_widget(im12)

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
