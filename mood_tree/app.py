import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.modules import inspector
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screenmanager import MDScreenManager

from mood_tree import config

# Import your screen classes BEFORE loading KV
from mood_tree.screens.home import HomeScreen  # noqa: F401
from mood_tree.screens.intro import IntroScreen  # noqa: F401
from mood_tree.widgets.navbar import NavBar  # noqa: F401


class MyScreenManager(MDScreenManager):
    pass

class MoodTreeApp(MDApp):
    # KV_DIRS = [config.KV_PATH]
    # DEBUG = True
    # def __init__(self, *args):
    #     super(MoodTreeApp, self).__init__(*args)

    # def build_app(self, first=False):
    #     # self.manager_screens = MyScreenManager()
    #     # return self.manager_screens
    #     main_kv_path = os.path.join(config.KV_PATH, "main.kv")
    #     return Builder.load_file(main_kv_path)
    KV_FILES = [
        os.path.join(config.KV_PATH, "main.kv"),
        os.path.join(config.KV_PATH, "home.kv"),
        os.path.join(config.KV_PATH, "intro.kv"),
        os.path.join(config.KV_PATH, "navbar.kv"),
    ]

    # Watch for changes in these directories
    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive": True}),
    ]

    # Optional: skip __pycache__ and compiled files
    AUTORELOADER_IGNORE_PATTERNS = ["*.pyc", "*__pycache__*"]

    DEBUG = True  # Enable hot reload

    def build_app(self):
        # ❗ Do NOT load kv manually — hotreload does it for you!
        # Just return the root widget defined in main.kv
        return Builder.load_file(os.path.join(config.KV_PATH, "main.kv"))
    
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        print("hello32")
        self.root.ids.screen_manager.current = item.navigate_to

    def on_start(self):
        self.fps_monitor_start()
        inspector.create_inspector(Window, self)  # This is a tool for inspecting elements
