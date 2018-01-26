from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
 
class click(BoxLayout):
    search_input = ObjectProperty()
    def do_clisk(self):
        print(self.search_input.text)
 
class WeatherApp(App):
    pass
 
if __name__ == '__main__':
    WeatherApp().run()
