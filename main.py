from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text='Merhaba Dünya! 🎉',
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.2, 0.6, 1, 1)
        )

if __name__ == '__main__':
    MyApp().run()
