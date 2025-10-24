from datetime import datetime

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class DateWidget(BoxLayout):
    current_date = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Format: weekday name, month, day number
        self.current_date = datetime.now().strftime("%A, %B %d")
