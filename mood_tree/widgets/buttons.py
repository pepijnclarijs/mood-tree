from kivy.properties import ListProperty, StringProperty
from kivymd.uix.button import MDButton

from mood_tree.config import AppConfig


class GeneralScreenNavigateButton(MDButton):
    target_screen = StringProperty(None)
    button_color = ListProperty(AppConfig.COLOR_SOFT_CORAL)
    button_text = StringProperty("Button!")
