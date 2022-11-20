"""
CP1404/CP5632
squaring number
Mason McKenzie
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class SquareNumberApp(App):
    """ SquareNumberApp is The Kivy Program used to square a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "SQUARE NUMBER"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass
SquareNumberApp().run()