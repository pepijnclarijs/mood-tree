from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView

Builder.load_string(
"""
<ScrollableLabel>:
    text: str('some really really long string ' * 2)
    Label:
        text: root.text
        font_size: 50
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
"""
)

class ScrollableLabel(ScrollView):
    text = StringProperty('')


def main():
    runTouchApp(ScrollableLabel())

if __name__ == "__main__":
    main()
