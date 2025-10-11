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


class MyScreenManager(MDScreenManager):
    pass

class MoodTreeApp(MDApp):
    # KV_FILES = [
    #     os.path.join(config.KV_PATH, "main.kv"),
    #     os.path.join(config.KV_PATH, "home.kv"),
    #     os.path.join(config.KV_PATH, "intro.kv"),
    #     os.path.join(config.KV_PATH, "navbar.kv"),
    # ]
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
    
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        print(f"item.navigate_to={item.navigate_to}")
        self.root_element.ids.screen_manager.current = item.navigate_to

    def on_start(self):
        print("=== DEBUG ROOT ===")
        print("root repr:", self.root)
        print("root type:", type(self.root))
        print("root ids keys:", list(getattr(self.root, "ids", {}).keys()))
        print("root children count:", len(self.root.children))
        for i, c in enumerate(self.root.children):
            print(f" child[{i}] repr: {c!r}")
            print(f" child[{i}] type: {type(c)}")
            print(f" child[{i}] ids keys: {list(getattr(c, 'ids', {}).keys())}")
        print(self.root.children[0].ids)
        print("==================")
        self.root_element = self.root.children[0]
        self.fps_monitor_start()
        inspector.create_inspector(Window, self)  # This is a tool for inspecting elements
