import random

from kivy.app import App
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):
    label_size = NumericProperty(200)
    text_color = ListProperty([1,0,0,1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)
    
    def change_label_color(self, *args):
        self.text_color = [random.random() for i in range(3)] + [1]

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()
    
if __name__ == "__main__":
    TutorialApp().run()