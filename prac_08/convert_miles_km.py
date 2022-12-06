"""
CP1404/CP5632
convert_miles_km
Mason McKenzie
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.61


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """This creates the Kivy app using the .kv file."""
        self.title = "Converting Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def control_increment(self, text, change):
        """controls the buttons pressed"""
        print("control increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)


    def control_calculate(self, text):
        """controls the calculation"""
        print("control calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def convert_to_number(text):
        try:
            return float(text)  # TURNS TEXT INTO A FLOAT
        except ValueError:
            return 0

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)



MilesConverterApp().run()
