import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from mood_tree import config

# Import your screen classes BEFORE loading KV
from mood_tree.screens.home import HomeScreen  # noqa: F401
from mood_tree.screens.intro import IntroScreen  # noqa: F401


class MyScreenManager(ScreenManager):
    pass

class MoodTreeApp(MDApp):
    def build(self):
        # Load the kv files.
        return Builder.load_file(os.path.join(config.KV_PATH, "main.kv"))    


    def on_start(self):
        self.fps_monitor_start()
