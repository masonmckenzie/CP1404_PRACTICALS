from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def control_clear(self):
        print("TEST")
        self.root.ids.output_label.text = "Please Enter Your Name"
        self.root.ids.input_name.text = " "

    def control_greet(self):
        """greets user"""
        print("TEST")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()