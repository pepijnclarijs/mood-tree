from kivymd.app import MDApp

class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return 0

def main():
    print("Hello from mood-tree!")


if __name__ == "__main__":
    App.run()
