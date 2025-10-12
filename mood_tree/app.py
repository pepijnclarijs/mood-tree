import os

from kivy.core.window import Window
from kivy.lang import Builder  # noqa: F401
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
    KV_FILES = [
        os.path.join(root, file)
        for root, _, files in os.walk(config.KV_PATH)
        for file in files if file.endswith(".kv")
    ]

    # Watch for changes in these directories
    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive": True}),
    ]

    # Optional: skip __pycache__ and compiled files
    AUTORELOADER_IGNORE_PATTERNS = ["*.pyc", "*__pycache__*"]

    DEBUG = True  # Enable hot reload

    def build_app(self, first=False):
        main_kv_file = os.path.join(config.KV_PATH, "main.kv")
        if main_kv_file in Builder.files:
            Builder.unload_file(main_kv_file)
        print(f"Builder.files={Builder.files}")
        print(f"self.KV_FILES={self.KV_FILES}")
        return Builder.load_file(main_kv_file)

    def apply_state(self, state):
        """Override this stub method to run custom code upon hot reload."""

        super().apply_state(state)
        
        # Refresh root_element to point to the newly created root
        if self.root and self.root.children:
            self.root_element = self.root.children[0]
            print("Updated root_element:", self.root_element)
    
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        print("root_element:", self.root_element)
        print("root children:", self.root.children)
        print("root_element in root.children?", self.root_element in self.root.children)
        print("screen_manager:", self.root_element.ids.get("screen_manager"))

        self.root_element.ids.screen_manager.current = item.navigate_to

    def on_start(self):
        self.root_element = self.root.children[0]
        self.fps_monitor_start()
        inspector.create_inspector(Window, self)  # This is a tool for inspecting elements
