# from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy_reloader.app import App  # For development


class TutorialApp(App):
    def build(self):
        root = FloatLayout()
        self.scatter = Scatter(size_hint=(None, None), size=(300, 300))

        # Load image  
        self.img = Image(source="crashcourse/lesson2/random_image.jpg", size=self.scatter.size, pos=self.scatter.pos)
        self.scatter.add_widget(self.img)
        root.add_widget(self.scatter)

        # Initial centering after layout is ready
        Clock.schedule_once(self.update_scatter_pos, 0)

        # Keep Scatter centered on window resize
        Window.bind(on_resize=self.on_window_resize)

        return root

    def update_scatter_pos(self, dt=None):
        """Center the Scatter in its parent and position the image at (0,0) inside it."""
        parent_size = self.scatter.parent.size
        scatter_size = self.scatter.size
        pos_x = (parent_size[0] - scatter_size[0]) / 2
        pos_y = (parent_size[1] - scatter_size[1]) / 2
        self.scatter.pos = (pos_x, pos_y)
        self.img.pos = (0, 0)

    def on_window_resize(self, window, width, height):
        """Keep Scatter centered when window is resized."""
        self.update_scatter_pos()


if __name__ == "__main__":
    TutorialApp().run()
