import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from mood_tree import config
from mood_tree.screens.home import HomeScreen
from mood_tree.screens.intro import IntroScreen


class MyScreenManager(ScreenManager):
    pass

class MoodTreeApp(MDApp):
    def build(self):
        # Load the kv files.
        Builder.load_file(os.path.join(config.KV_PATH, "home.kv"))    
        
        sm = MyScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(IntroScreen())
        
        return sm
