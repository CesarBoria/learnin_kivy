from kivy.app import App

from game_screen import GameScreen


class MyApp(App):
    def build(self):
        ob = GameScreen()
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
