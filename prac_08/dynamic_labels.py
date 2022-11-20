from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "BOX_LAYOUT_DEMO"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("TEST")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        print("TEST")
        self.root.ids.output_label.text = "Please Enter Your Name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()