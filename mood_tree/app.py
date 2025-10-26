import os

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder  # noqa: F401
from kivy.metrics import sp
from kivy.modules import inspector
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screenmanager import MDScreenManager

from mood_tree.config import AppConfig

# Import your screen classes BEFORE loading KV
from mood_tree.screens.add_entry import AddEntry  # noqa: F401
from mood_tree.screens.home import HomeScreen  # noqa: F401
from mood_tree.screens.intro import IntroScreen  # noqa: F401
from mood_tree.widgets.buttons import GeneralScreenNavigateButton  # noqa: F401
from mood_tree.widgets.navbar import NavBar  # noqa: F401
from mood_tree.widgets.utility_widgets import DateWidget  # noqa: F401


class MyScreenManager(MDScreenManager):
    pass

class MoodTreeApp(MDApp):
    KV_FILES = [
        os.path.join(root, file)
        for root, _, files in os.walk(AppConfig.KV_PATH)
        for file in files if file.endswith(".kv")
    ]
    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive": True}),
    ]
    AUTORELOADER_IGNORE_PATTERNS = ["*.pyc", "*__pycache__*"]
    DEBUG = True
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app_config = AppConfig()

    def build_app(self, first=False):
        self.register_custom_font()

        main_kv_file = os.path.join(AppConfig.KV_PATH, "main.kv")
        if main_kv_file in Builder.files:
            Builder.unload_file(main_kv_file)
        
        return Builder.load_file(main_kv_file)

    def register_custom_font(self):
        LabelBase.register(
            name="Inter",
            fn_regular=os.path.join(AppConfig.ASSETS_PATH, "fonts/inter_font.ttf")
        )

        self.theme_cls.font_styles["Inter"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "Inter",
                "font-size": sp(67),
            },
            "medium": {
                "line-height": 1.4,
                "font-name": "Inter",
                "font-size": sp(24),
            },
            "small": {
                "line-height": 1.2,
                "font-name": "Inter",
                "font-size": sp(10),
            },
        }

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
        """Method for handling navbar tab switches."""
        self.root_element.ids.screen_manager.current = item.navigate_to

    def on_start(self):
        self.root_element = self.root.children[0]
        inspector.create_inspector(Window, self)  # This is a tool for inspecting elements

