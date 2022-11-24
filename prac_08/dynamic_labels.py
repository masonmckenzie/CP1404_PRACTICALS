"""
CP1404/CP5632
dynamic_labels
Mason McKenzie
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "BOX_LAYOUT_DEMO"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def control_greet(self):
        print("CONTROL_TEST")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def control_clear(self):
        print("CONTROL_TEST")
        self.root.ids.output_label.text = "Please Enter Your Name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()