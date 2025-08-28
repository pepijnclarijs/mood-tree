from kivy.app import App
from kivy.uix.label import Label
from plyer import notification


class AndroidApp(App):
    def build(self):
        notification.notify(title='Some title', message='Some text')
        return Label(text="Hello from Kivy!")


if __name__ == "__main__":
    AndroidApp().run()