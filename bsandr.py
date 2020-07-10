from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.config import Config
Config.set('graphics','rizable', '0');
Config.set('graphics','width', '640');
Config.set('graphics','height', '480');

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        f1=FloatLayout(size=(300,300))
        f1.add_widget(Button(text="это кнопка",
            font_size=16,
            on_press= self.btn_press,
            background_color=[1,0,0,1],
            background_normal = '',
            size_hint = (.5,.25),
            pos=(640/2-160,480/2-(480*.25/2))))
        
        return f1
        
    def btn_press(self,instance):   
        instance.text="я нажата"
        
        
if __name__ == "__main__":
    MyApp().run()
